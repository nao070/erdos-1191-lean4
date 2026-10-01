from pathlib import Path
import subprocess,json,selectors,time,sys,os,signal
root='/Users/USER/Documents/ChatGPT/mathematics'
out=Path(sys.argv[1]);mode=sys.argv[2] if len(sys.argv)>2 else 'proxy'
skills_only=len(sys.argv)>3 and sys.argv[3]=='skills-only'
cmd=['codex','app-server','proxy'] if mode=='proxy' else ['codex','app-server','--stdio']
err=out.with_suffix('.stderr.log').open('w');p=subprocess.Popen(cmd,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=err,text=True,bufsize=1,start_new_session=True)
sel=selectors.DefaultSelector();sel.register(p.stdout,selectors.EVENT_READ)
result={'probe_pid':p.pid,'probe_process_group':p.pid,'command':cmd,'read_only_methods':['initialize','skills/list','mcpServerStatus/list'],'cwd':root,'responses':{}}
def send(x):p.stdin.write(json.dumps(x)+'\n');p.stdin.flush()
def call(i,method,params,timeout=20):
 send({'id':i,'method':method,'params':params});until=time.monotonic()+timeout
 while time.monotonic()<until:
  events=sel.select(min(1,until-time.monotonic()))
  if not events:
   if p.poll() is not None:raise RuntimeError('probe process exited '+str(p.returncode))
   continue
  line=p.stdout.readline()
  if not line:raise RuntimeError('probe stdout closed; exit '+str(p.poll()))
  j=json.loads(line)
  if j.get('id')==i:
   if 'error' in j:raise RuntimeError(json.dumps(j['error']))
   return j.get('result')
 raise TimeoutError(method+' timed out; no runtime conclusion')
try:
 result['responses']['initialize']=call(1,'initialize',{'clientInfo':{'name':'erdos1191_harness_install_probe','version':'1.0'},'capabilities':{'experimentalApi':True}})
 send({'method':'initialized','params':{}})
 result['responses']['skills/list']=call(2,'skills/list',{'cwds':[root],'forceReload':True})
 pages=[];cursor=None
 for n in range(0 if skills_only else 10):
  args={'threadId':'01a082ca-fbda-7cb3-a0c9-ffc50c175187','detail':'toolsAndAuthOnly','limit':100}
  if mode!='proxy':args.pop('threadId',None)
  if cursor:args['cursor']=cursor
  page=call(3+n,'mcpServerStatus/list',args,30)
  slim=[]
  for item in page.get('data',[]):
   tools=item.get('tools',{})
   if isinstance(tools,dict):names=list(tools)
   else:names=[x.get('name') for x in tools]
   slim.append({'name':item.get('name'),'authStatus':item.get('authStatus'),'tool_names':names,'tool_count':len(names),'other_returned_fields':list(item)})
  pages.append({'data':slim,'nextCursor':page.get('nextCursor')});cursor=page.get('nextCursor')
  if not cursor:break
 if not skills_only:result['responses']['mcpServerStatus/list']=pages
 result['status']='PASS'
except Exception as e:result['status']='PROBE_UNRESOLVED';result['error']=str(e)
finally:
 if p.poll() is None:p.terminate()
 try:p.wait(timeout=5)
 except subprocess.TimeoutExpired:p.kill();p.wait()
 result['probe_process_terminal']=True;result['probe_exit']=p.returncode
 try:os.killpg(p.pid,signal.SIGTERM)
 except ProcessLookupError:pass
 result['owned_group_stop_requested']=True;err.close();out.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'status':result['status'],'error':result.get('error'),'response_methods':list(result['responses']),'artifact':str(out)},ensure_ascii=False))
