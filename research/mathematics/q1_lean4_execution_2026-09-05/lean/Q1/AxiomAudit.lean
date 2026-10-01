import Q1.Equivalence
import Q1.Nonvacuity
import Q1.DirectMoment
import Q1.HaarShape
import Q1.DifferenceLabels
import Q1.SharedDifferenceBudget
import Q1.PhysicalLabelEnvelope
import Q1.MomentDemand

/- This module is a build target. Its declarations only audit the supporting results. -/

#print Erdos1191Q1.Positive
#print Erdos1191Q1.Sidon
#print Erdos1191Q1.countingSet
#print Erdos1191Q1.count
#print Erdos1191Q1.realCount
#print Erdos1191Q1.normalized
#print Erdos1191Q1.Original
#print Erdos1191Q1.IntegerSquared
#print Erdos1191Q1.Q1
#print Erdos1191Q1.Q1Integer
#print Erdos1191Q1.EventualLowerBound

#check Erdos1191Q1.original_iff_integerSquared
#check Erdos1191Q1.q1_iff_q1Integer
#check Erdos1191Q1.not_original_iff
#check Erdos1191Q1.not_q1_iff
#check Erdos1191Q1.admissible_exists

#print axioms Erdos1191Q1.Original
#print axioms Erdos1191Q1.Q1
#print axioms Erdos1191Q1.mem_countingSet_real
#print axioms Erdos1191Q1.original_iff_integerSquared
#print axioms Erdos1191Q1.q1_iff_q1Integer
#print axioms Erdos1191Q1.not_original_iff
#print axioms Erdos1191Q1.not_q1_iff
#print axioms Erdos1191Q1.admissible_exists

#check Erdos1191Q1.direct_gap_quadratic_moments
#check Erdos1191Q1.direct_point_quadratic_moments
#check Erdos1191Q1.path_correction_not_psd_witness
#print axioms Erdos1191Q1.direct_gap_quadratic_moments
#print axioms Erdos1191Q1.direct_point_quadratic_moments
#print axioms Erdos1191Q1.path_correction_not_psd_witness

#print Erdos1191Q1.threeJumpCore
#check Erdos1191Q1.directGapCoefficient_shift_gap
#check Erdos1191Q1.threeJumpCore_eq
#check Erdos1191Q1.threeJumpCore_lower
#check Erdos1191Q1.corrected_threeJumpCore_nonneg
#check Erdos1191Q1.directGapCoefficient_nonpos
#check Erdos1191Q1.opposite_two_jump_nonneg
#print axioms Erdos1191Q1.directGapCoefficient_shift_gap
#print axioms Erdos1191Q1.threeJumpCore_eq
#print axioms Erdos1191Q1.threeJumpCore_lower
#print axioms Erdos1191Q1.corrected_threeJumpCore_nonneg
#print axioms Erdos1191Q1.directGapCoefficient_nonpos
#print axioms Erdos1191Q1.opposite_two_jump_nonneg

#print Erdos1191Q1.PositiveDifferenceUnique
#print Erdos1191Q1.IsPositivePair
#print Erdos1191Q1.differenceLabel
#print Erdos1191Q1.prefixPositivePairs
#print Erdos1191Q1.prefixDifferenceMap
#check Erdos1191Q1.sidon_iff_positiveDifferenceUnique
#check Erdos1191Q1.differenceLabel_injOn
#check Erdos1191Q1.positivePairs_card_le_labels
#check Erdos1191Q1.positivePairs_image_card_eq
#check Erdos1191Q1.weighted_positivePairs_le_labels
#check Erdos1191Q1.selectedLabels_card_le
#check Erdos1191Q1.differenceLabel_fiber_card_le_one
#check Erdos1191Q1.prefixDifferenceMap_injective
#check Erdos1191Q1.prefix_selectedLabels_card_le
#check Erdos1191Q1.prefixPositivePairs_card_le
#print axioms Erdos1191Q1.sidon_iff_positiveDifferenceUnique
#print axioms Erdos1191Q1.differenceLabel_injOn
#print axioms Erdos1191Q1.positivePairs_card_le_labels
#print axioms Erdos1191Q1.positivePairs_image_card_eq
#print axioms Erdos1191Q1.weighted_positivePairs_le_labels
#print axioms Erdos1191Q1.selectedLabels_card_le
#print axioms Erdos1191Q1.differenceLabel_fiber_card_le_one
#print axioms Erdos1191Q1.prefixDifferenceMap_injective
#print axioms Erdos1191Q1.prefix_selectedLabels_card_le
#print axioms Erdos1191Q1.prefixPositivePairs_card_le

#print Erdos1191Q1.internalPairs
#print Erdos1191Q1.internalLabels
#print Erdos1191Q1.labelKernel
#print Erdos1191Q1.labelExpenditure
#print Erdos1191Q1.shadowRow
#print Erdos1191Q1.labelShadow
#print Erdos1191Q1.shadowLocations
#check Erdos1191Q1.internalLabels_disjoint
#check Erdos1191Q1.labelKernel_eq_shift_sum
#check Erdos1191Q1.total_labelKernel
#check Erdos1191Q1.shared_label_budget
#check Erdos1191Q1.sum_labelShadow
#check Erdos1191Q1.sum_sq_labelShadow
#check Erdos1191Q1.shadow_cauchy_capacity
#check Erdos1191Q1.shadowLocations_disjoint_of_actual_labels
#check Erdos1191Q1.shadow_interval_capacity
#check Erdos1191Q1.shared_interval_demand_budget
#print axioms Erdos1191Q1.internalLabels_disjoint
#print axioms Erdos1191Q1.labelKernel_eq_shift_sum
#print axioms Erdos1191Q1.total_labelKernel
#print axioms Erdos1191Q1.shared_label_budget
#print axioms Erdos1191Q1.sum_labelShadow
#print axioms Erdos1191Q1.sum_sq_labelShadow
#print axioms Erdos1191Q1.shadow_cauchy_capacity
#print axioms Erdos1191Q1.shadowLocations_disjoint_of_actual_labels
#print axioms Erdos1191Q1.shadow_interval_capacity
#print axioms Erdos1191Q1.shared_interval_demand_budget

#print Erdos1191Q1.physicalEnvelope
#print Erdos1191Q1.intervalLabelDemand
#print Erdos1191Q1.maskedEpochKernel
#print Erdos1191Q1.epochLabelSupport
#check Erdos1191Q1.disjoint_label_demand_envelope
#check Erdos1191Q1.actual_blocks_envelope_budget
#check Erdos1191Q1.intervalLabelDemand_le
#check Erdos1191Q1.growing_prefix_interval_envelope
#check Erdos1191Q1.actual_blocks_envelope_accounting
#print axioms Erdos1191Q1.le_physicalEnvelope
#print axioms Erdos1191Q1.physicalEnvelope_nonneg
#print axioms Erdos1191Q1.physicalEnvelope_eq_zero_of_notMem
#print axioms Erdos1191Q1.disjoint_label_envelope_budget
#print axioms Erdos1191Q1.disjoint_label_demand_envelope
#print axioms Erdos1191Q1.actual_blocks_envelope_budget
#print axioms Erdos1191Q1.intervalCapacity_pos
#print axioms Erdos1191Q1.intervalLabelDemand_le
#print axioms Erdos1191Q1.internalLabels_mem_interval
#print axioms Erdos1191Q1.maskedEpochKernel_nonneg
#print axioms Erdos1191Q1.maskedEpochKernel_supported
#print axioms Erdos1191Q1.maskedEpochKernel_eq_on_actual_labels
#print axioms Erdos1191Q1.weighted_interval_demand_le_epoch
#print axioms Erdos1191Q1.growing_prefix_interval_envelope
#print axioms Erdos1191Q1.label_envelope_accounting
#print axioms Erdos1191Q1.physicalEnvelope_slack_nonneg
#print axioms Erdos1191Q1.actual_blocks_envelope_accounting

/- The moment demand is derived from the actual signed shadow and its first moment. -/
#print axioms Erdos1191Q1.coordinateVariance
#print axioms Erdos1191Q1.labelFirstMoment
#print axioms Erdos1191Q1.shadowRow_firstMoment
#print axioms Erdos1191Q1.labelShadow_firstMoment
#print axioms Erdos1191Q1.labelShadow_centered_firstMoment
#print axioms Erdos1191Q1.shadow_firstMoment_cauchy
#print axioms Erdos1191Q1.shadowMomentLowerBound
#print axioms Erdos1191Q1.shadowMomentLowerBound_le
#print axioms Erdos1191Q1.momentKernel
#print axioms Erdos1191Q1.momentKernel_eq_pairs
#print axioms Erdos1191Q1.momentKernel_nonneg
#print axioms Erdos1191Q1.momentKernel_supported
#print axioms Erdos1191Q1.momentExpenditure
#print axioms Erdos1191Q1.momentExpenditure_eq
#print axioms Erdos1191Q1.moment_shadow_energy
#print axioms Erdos1191Q1.matrixMassRawDemand
#print axioms Erdos1191Q1.momentRawDemand
#print axioms Erdos1191Q1.momentRawDemand_sub_mass
#print axioms Erdos1191Q1.momentDemand
#print axioms Erdos1191Q1.momentRawDemand_le
#print axioms Erdos1191Q1.momentDemand_le
#print axioms Erdos1191Q1.shadowLocations_subset_interval
#print axioms Erdos1191Q1.interval_momentDemand_le
#print axioms Erdos1191Q1.maskedMomentKernel
#print axioms Erdos1191Q1.maskedMomentKernel_nonneg
#print axioms Erdos1191Q1.maskedMomentKernel_supported
#print axioms Erdos1191Q1.maskedMomentKernel_eq_on_actual
#print axioms Erdos1191Q1.shared_momentDemand_envelope
