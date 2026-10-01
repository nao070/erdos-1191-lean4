from pathlib import Path
import datetime
import hashlib
import json

BASE = Path(__file__).resolve().parents[1]

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def read(rel):
    return json.loads((BASE / rel).read_text())

def write(rel, data):
    (BASE / rel).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')

prior_rel = 'evidence/goal9_reviewed_research.json'
prior = read(prior_rel)
assert sha(BASE / prior_rel) == '054629d4e4862fc4f62edc7883d9b8d8e8754c18972d6c6c738b9e5f3386d43d'
governance = {'OUTCOME.json', 'RESEARCH_STATUS.md'}
for rel, expected in prior['files'].items():
    if rel not in governance:
        assert sha(BASE / rel) == expected, rel

versions = {
    'eligible_capacity_packing_closure': '1bbe91da5091f59c1ecaf32cd70a8e48fd22bc7e174dd09c2831614d41e34964',
    'triple_potential_productive_source': 'f9be618684b2ed933b480f4107c0ccdbddffd309339e7d63db831d511cf920ff',
    'triple_source_remainder_analysis': '6476aca5330fa7a368b40872650994290c97f2456899cb73f9fccb67c68eb775',
    'causal_fourier_coefficient_route': '344529631f892c8577f7caa45e440b422fb9de8f3a6d06c3a52031fbfb98a820',
}
reviews = []
for name, expected in versions.items():
    source = 'research/' + name + '.md'
    review = 'research/' + name + '_review.md'
    assert sha(BASE / source) == expected, source
    assert expected in (BASE / review).read_text(), review
    reviews.append({'source': source, 'source_sha256': expected, 'review': review,
                    'review_sha256': sha(BASE / review), 'status': 'PASS',
                    'scope': 'Independent analytical proof review, not Lean or Q1 verification.'})

goal_observation = read('evidence/goal10_goal_state_observation.json')
goal_state = goal_observation['result']['goal']['status']
assert goal_state == 'active', goal_state
formal = read('lean/evidence/sidon_collision_determination_result.json')
binding = read('evidence/goal10_sidon_parent_binding.json')
assert formal['status'] == binding['status'] == 'PASS'
assert formal['declaration_count'] == 7 and binding['combined_distinct_supporting_scope'] == 132
now = datetime.datetime.now(datetime.timezone.utc)
jst = now.astimezone(datetime.timezone(datetime.timedelta(hours=9)))

outcome = read('OUTCOME.json')
outcome.update({
    'status': 'Q1_UNRESOLVED', 'goal_status': goal_state,
    'latest_verified_supporting_audit_count': 132,
    'requested_completion_gate_satisfied': False,
    'resolution_theorem': None, 'proof_of_original_Q1': False,
    'proof_of_negation_of_original_Q1': False,
    'model_configuration_changed': False, 'external_interruption': None,
    'research_updated_at': now.isoformat(),
    'current_input_identity': 'evidence/goal10_primary_byte_identity.json',
    'parent_saved_exact_binding_record': 'evidence/goal10_sidon_parent_binding.json',
    'previous_reviewed_research_snapshot': prior_rel,
    'current_reviewed_research_snapshot': 'evidence/goal10_reviewed_research.json',
    'primary_byte_recheck': 'evidence/goal10_primary_byte_identity.json',
    'latest_primary_metadata_inventory': 'evidence/goal10_primary_byte_identity.json',
    'latest_lean_source_identity': 'evidence/goal10_sidon_parent_binding.json',
    'latest_formal_verification_record': 'lean/evidence/sidon_collision_determination_result.json',
    'latest_formal_checker_record': 'lean/evidence/sidon_collision_determination_checker.run.json',
    'latest_formal_scope': 'One actual finite endpoint-record definition and six theorems derive the far gap, far-pair uniqueness, exact membership, disjointness, near-coordinate injection and cardinality at most K cubed. Full orbit, geometry, energy/source and Q1 remain unformalized.',
    'latest_replay_scope': 'New module targeted build, explicit seven-name axiom audit and imported-environment Lean checker each have actual exit0. No full dependency replay, independent external kernel, combined132 audit or final Q1 release.',
    'supporting_audit_count_scope': '132 distinct supporting declarations across seven saved scopes:82+16+5+16+2+4+7. No combined132 run; old aggregate unchanged.',
    'latest_goal_turn_classification': 'progress: four new reviewed analytical notes, an actual productive defect-financed Gram source, precise lattice/residue/PSD limitations and causal coefficient identity; seven new actual Sidon declarations built/audited/replayed. Original Q1 unresolved.',
    'goal_status_observation': 'evidence/goal10_goal_state_observation.json',
    'goal_status_cause': 'Active continuation confirmed by live service; parent did not call update_goal.',
    'goal_status_not_a_mathematical_blocker_assessment': True,
    'automatic_continuation_requires_user_goal_resume': False,
    'ongoing_not_yet_reviewed': [],
    'active_research_routes': [
        'Uniform actual eligible-capacity upper bound, equivalent to universal bounded frozen residual on a dilation-closed class.',
        'Restricted growing residue information and one-source allocation with a cap-forced comparison beyond exact singleton recovery.',
        'Actual full geometry-defect representation enabling productive recursion without copying its scalar allowance.',
        'Exact causal analytic coefficient functional and a genuinely applicable order-sensitive Fourier estimate.',
        'Actual Sidon multiset/rank/orbit/energy formal bridge and eventual final original-Q1 theorem.',
    ],
    'next_mathematical_obligations': [
        'Prove a uniform actual eligible-capacity bound or a nontrivial fixed-cap comparison for explicitly restricted residue information; arbitrary-resolution zero residual is tautological.',
        'Find a genuine full-G representation or joint allocation reducing a real residual. The orthogonal-fiber and scalar gammaJ PSD debit proposals fail on an actual payable Sidon pair.',
        'Investigate a stronger bound for the exact causal coefficient functional; ordinary point-frequency Carleson does not directly control birth-ordered gap sums.',
        'Formalize the remaining actual multiset orbit/energy/source aggregation when the global argument is established.',
        'Obtain complete original-Q1 proof or actual infinite fixed-onset counterexample, then final Lean theorem, clean release build and semantic axiom audit.',
    ],
})
for name in formal['declarations']:
    if name not in outcome['verified_supporting_declarations']:
        outcome['verified_supporting_declarations'].append(name)
add_results = [
    'Frozen moment packing loses at least half of eligible capacity after dilation6, and primitive spectator dilation16 retains a finite3/64 comparison; all capped-history implications remain conditional.',
    'Same-shadow residue projection preserves one trace and one pair budget; any fixed finite modulus family retains a dilation obstruction, whereas unrestricted moduli exactly recover all raw eligible capacity.',
    'Concrete fixed and component-fraction residue Schur masks are PSD, nonnegative and compatible, with all birth/output clocks retained.',
    'Actual triple-fiber square-root Gram Theta has trace at most5/36 and full-tail mass at most1/18; its cost is financed by G with constant zeta2/6+7/144.',
    'One fixed Theta component spent across actual future physical cells has a Hardy demand fraction log(7/5)/(192C), yielding nonsummable good-window actual demands without budget reuse.',
    'Actual positive Sidon fixture1,2,4,11,15 disproves orthogonal-fiber and all scalar gammaJ PSD remainders for the specified productive Gram; other full-G representations remain open.',
    'Exact signed analytic coefficient identity retains actual b<i<r eligibility; ordinary Fourier partials control point polynomials, while the elementary actual causal bound still has harmonic cost.',
]
for item in add_results:
    if item not in outcome['latest_nonformal_reviewed_results']:
        outcome['latest_nonformal_reviewed_results'].append(item)
for item in ['Lattice and primitive frozen-packing bounds, residue projection/refinement and compatible masked Gram sources',
             'Triple-potential productive Gram, full defect financing, physical-cell Hardy allocation and PSD remainder obstructions',
             'Exact causal analytic coefficient identity and stronger uniform order-sensitive estimate']:
    if item not in outcome['not_lean_verified']:
        outcome['not_lean_verified'].append(item)
for key, item in [('additional_formal_verification_records','lean/evidence/sidon_collision_determination_result.json'),
                  ('additional_parent_formal_bindings','evidence/goal10_sidon_parent_binding.json')]:
    if item not in outcome[key]: outcome[key].append(item)
write('OUTCOME.json', outcome)

status_path = BASE / 'RESEARCH_STATUS.md'
status = status_path.read_text()
marker = '## 2026-09-05 22:20 JST の現在地'
assert marker in status
section = f'''## {jst.strftime('%Y-%m-%d %H:%M')} JST の現在地

**原 Q1 の完全証明・完全反証、最終 Lean theorem は未達。Goal は active。**
親は `update_goal` を呼んでいない。指定モデル・推論設定を変更していない。
実状態は `evidence/goal10_goal_state_observation.json` に保存した。

指定 ZIP と MASTER、Downloads の C143 V2 bank、最新の bound follow-up の
内容は引き続き一致する。34件の限定した metadata inventory に新しい置換入力はない。
同一 bank の90,600,510件 pricing replay は再実行せず、C139 台帳も現在地にしていない。
根拠は `evidence/goal10_primary_byte_identity.json`。

実際の Sidon 端点から far pair の一意性を導き、有限衝突集合から近い3座標への
単射と `card <= |K|^3` を形式化した。新しい **7宣言**の対象 build・全名の公理監査・
import 環境の Lean checker は実 exit 0。親も実ソース、23/31件の実行時 binding、
公理と全出力、生成物、旧281ファイルの一致を独立に読み戻した。
`evidence/goal10_sidon_parent_binding.json` と
`research/sidon_collision_determination_formal_scope.md` に範囲を記録した。
補助範囲は **計132宣言、7つの別々の保存済み監査**で、一括132宣言監査ではない。
全 orbit・geometry・energy・source の統合、原 Q1、完成 release は未検証のまま。

解析では、固定した投影の最適配分にも、格子拡大で一様な損失が残ると証明した。
1点を加えて gcd を1にしても残り、固定した有限個の modulus を使っても回避できない。
一方、同じ二つの shadow を剰余類ごとに投影する改善を構成した。無制限に細分化すると
需要と実容量が一致するだけの恒等式になり、そのゼロ残差は Q1 を閉じない。
これは `research/eligible_capacity_packing_closure.md` にある。

三項和の実 fiber から、新しい非負 PSD source Theta を構成した。総 trace <=5/36、
有限制限の将来 tail <=1/18 を保ち、既存の geometry defect で費用を評価できる。
同一成分を実際の長い将来区間へ一度ずつ配分し、Hardy 評価から非可和な実需要を得た。
ただし追加後の残差は旧残差と新残差の和であり、元の未制御量を自動的には減らさない。
`research/triple_potential_productive_source.md` に式と固定 cap・有限 horizon を残した。
二つの自然な PSD 残余候補は、実際の正整数 Sidon 集合 {{1,2,4,11,15}} で否定できる。
他の full-defect 表現は否定していない。詳細は `research/triple_source_remainder_analysis.md`。

別経路では、実際の順序を保つ Fourier 係数の恒等式として利用可能量を表した。
通常の最大値定理をそのまま差分の追加順へ適用することはできず、現状の上界は調和和。
`research/causal_fourier_coefficient_route.md` に正確な式と一次文献の適用範囲を記録した。
以上4本の新解析は独立レビュー済みで、親の再導出は `research/goal10_parent_review.md`。
版の結び付けは `evidence/goal10_reviewed_research.json`。

次は実容量の一様上界、制限した剰余類情報による非自明な比較、予算を複製しない
full-defect 表現、または実順序の Fourier 評価を進める。これらの補助結果と検証を
completion と扱わず、原 Q1 と最終 Lean 検証という同じ条件の下で継続する。

## 2026-09-05 22:20 JST の履歴
'''
status_path.write_text(status.replace(marker, section, 1))

paths = set(prior['files'])
paths.add(prior_rel)
for pattern in ['evidence/goal10*', 'lean/evidence/sidon_collision_determination_*']:
    paths.update(str(p.relative_to(BASE)) for p in BASE.glob(pattern) if p.is_file())
paths.update(['lean/Q1/SidonCollisionDetermination.lean',
              'research/sidon_collision_determination_formal_scope.md', 'research/goal10_parent_review.md'])
for row in reviews: paths.update([row['source'], row['review']])
paths.update('lean/' + rel for rel in formal['compiled_artifact_sha256'])
snapshot_rel = 'evidence/goal10_reviewed_research.json'
paths.discard(snapshot_rel)
files = {rel: sha(BASE / rel) for rel in sorted(paths)}
snapshot = {
    'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'status': 'REVIEWED_PROGRESS_Q1_UNRESOLVED',
    'scope': 'Four new reviewed analytical sources and one actual Sidon finite-record module with seven supporting declarations. No completion claim.',
    'files': files, 'prior_research_snapshot': prior_rel,
    'prior_snapshot_sha256': sha(BASE / prior_rel),
    'prior_nongovernance_sources_unchanged': len(prior['files']) - 2,
    'intentional_governance_updates': sorted(governance),
    'independent_review_version_bindings': reviews,
    'parent_mathematical_review': 'research/goal10_parent_review.md',
    'new_formal_parent_bindings': ['evidence/goal10_sidon_parent_binding.json'],
    'new_formal_record': 'lean/evidence/sidon_collision_determination_result.json',
    'formal_scope_counts': {**prior['formal_scope_counts'], 'SidonCollisionDetermination': 7},
    'distinct_audited_supporting_declarations': 132,
    'separate_saved_audit_scopes': 7,
    'new_substantive_lean_executions_this_continuation': {'targeted_builds': 1, 'explicit_axiom_audits': 1, 'imported_environment_checker_runs': 1},
    'new_supporting_declarations': 7, 'combined_132_declaration_audit_executed': False,
    'new_module_imported_by_unchanged_aggregate_Q1': False,
    'lean_scope_limit': 'Actual local finite record determination and counting only. No full orbit, geometric/energy/global source theorem, Q1, final release build, complete dependency replay or independent external checker.',
    'failed_substantive_lean_execution_this_continuation': False,
    'primary_byte_identity': 'evidence/goal10_primary_byte_identity.json',
    'primary_literature_scope': 'evidence/goal10_primary_literature_scope.json',
    'unresolved_global_obligation': outcome['next_mathematical_obligations'],
    'q1_resolved': False, 'goal_status': goal_state,
    'goal_status_observation': 'evidence/goal10_goal_state_observation.json',
    'goal_turn_classification': 'progress', 'model_configuration_changed': False,
    'parent_called_update_goal_this_turn': False,
}
write(snapshot_rel, snapshot)
for rel, expected in files.items(): assert sha(BASE / rel) == expected, rel
print(json.dumps({'snapshot': snapshot_rel, 'sha256': sha(BASE / snapshot_rel), 'file_count': len(files),
                  'independent_review_bindings': len(reviews), 'supporting_scope': 132,
                  'goal_status': goal_state, 'q1_resolved': False}, ensure_ascii=False))
