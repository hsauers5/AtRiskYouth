class Scoring:


  # developed based on the most highly correlated factors to opioid use per the CDC 2017 dataset
  def get_opiate_risk_score(student):
    
    score = 0

    if student.physical_fights > 2: 
      score += 1
    if student.tried_cigs < 2: 
      score += 1
    if student.smokes_cigs > 1: 
      score += 1
    if student.cigs_per_day > 2: 
      score += 1
    if student.days_vaping > 2: 
      score += 1
    if student.cigar_use > 2: 
      score += 1
    if student.quit_tobacco_attempt >= 2: 
      score += 1
    if student.days_drinking > 2: 
      score += 1
    if student.current_drinking > 2: 
      score += 1
    if student.binge_drinking > 2: 
      score += 1
    if student.max_drinks > 6: 
      score += 1
    if student.tried_marijuana > 3: 
      score += 1
    if student.current_marijuana > 2: 
      score += 1
    if student.sex_partners_total > 3: 
      score += 1
    if student.sex_partners_recent > 2: 
      score += 1
    if student.condom_use > 2: 
      score += 1
    if student.drive_marijuana > 2: 
      score += 1
    if student.hallucinogens_ever > 2: 
      score += 1
    if student.ever_injected >= 2: 
      score += 1

    return score
