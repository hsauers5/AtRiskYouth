from Scoring import Scoring
# data structure for survey answers
class Student:

  raw_data = []

  # raw variables
  race = -1 # ???
  age = -1 # 1: <=12, 2:13, 3:14, 4:15, 5:16, 6:17, 7:18+
  sex = -1 # 1 female, 2 male
  grade = -1 # 1:9th, 2:10th, 3:11th, 4:12th, 5:other
  hispanic = -1 # 1:yes, 2:no
  seatbelt = -1 # 1:never thru 5:always
  ride_with_drunk = -1 # 1:0 thru 5:6+times
  drive_drunk = -1 # 1&2:0 thru 6:6+times
  drive_text = -1 # 1&2:0 thru 8:every day
  carry_weapon = -1 # 1:0 thru 5:6+times
  weapon_at_school = -1 # 1:0 thru 5:6+times
  carry_gun = -1 # 1:0 thru 5:6+times
  school_notsafe = -1 # 1:0 thru 5:6+times
  school_threats = -1 # 1:0 times thru 8:12+
  physical_fights = -1 # 1:0 times thru 8:12+
  fights_at_school = -1 # 1:0 times thru 8:12+
  been_raped = -1 # 1:yes 2:no
  been_forced_sexually = -1 # 1:0 thru 5:6+times
  date_rape_assault = -1 # 1&2:0 thru 6:6+times
  so_violence = -1 # 1&2:0 thru 6:6+times
  bullied_school = -1 # 1:yes 2:no
  bullied_cyber = -1 # 1:yes 2:no
  sad_hopeless = -1 # 1:yes 2:no
  consider_suicide = -1 # 1:yes 2:no
  plan_suicide = -1 # 1:yes 2:no
  attempt_suicide = -1 # 1:0 thru 5:6+times
  suicide_injury = -1 # 1:NO ATTEMPT, 2:yes, 3:no
  tried_cigs = -1 # 1:yes, 2:no
  age_cigs = -1 #1:8 or younger thru 7:17+
  smokes_cigs = -1 # 1:0 thru 7:every day
  cigs_per_day = -1 # 1:none, 2:<1, 3:1, thru 7:20+
  vaping = -1 # 1:yes, 2:no
  days_vaping = -1 # 1:0 thru 7:every day
  acquire_vape = -1 # 1:no use, 2:store, 3:internet, 4:friend, 5:borrowed, 6:18+ gift, 7:stole, 8:other
  smokeless_tobacco = -1 # 1:0 thru 7:every day
  cigar_use = -1 # 1:0 thru 7:every day
  quit_tobacco_attempt = -1 #1:no use, 2:yes, 3:no
  days_drinking = -1 # 1:0 thru 7:100+
  age_drinking = -1 #1:8 or younger thru 7:17+
  current_drinking = -1 # 1:0 thru 7:every day
  acquire_alcohol = -1 # 1:no use, 2:store, 3:internet, 4:friend, 5:borrowed, 6:18+ gift, 7:stole, 8:other
  binge_drinking = -1 # 1:0 thru 7:20+
  max_drinks = -1 # 1:none thru 8:10+
  tried_marijuana = -1 # 1:0 thru 7:100+
  age_marijuana = -1 # 1:8 or younger thru 7:17+
  current_marijuana = -1 # 1:0 thru 6:40+
  ever_cocaine = -1 # 1:0 thru 6:40+
  ever_inhalants = -1 # 1:0 thru 6:40+
  ever_heroin = -1 # 1:0 thru 6:40+
  ever_meth = -1 # 1:0 thru 6:40+
  ever_ecstasy = -1 # 1:0 thru 6:40+
  ever_spice = -1 # 1:0 thru 6:40+
  ever_steroids = -1 # 1:0 thru 6:40+
  ever_opioids = -1 # 1:0 thru 6:40+
  ever_injected = -1 # 1:none, 2:1, 3:2+
  drugs_at_school = -1 # 1:yes, 2:no
  had_sex = -1 # 1:yes, 2:no
  age_of_sex = -1 # 1:8 or younger thru 7:17+
  sex_partners_total = -1 # 1:none thru 7:6+
  sex_partners_recent = -1 # 1:none thru 7:6+
  sex_intoxicated = -1 # 1:never had, 2:yes, 3:no
  condom_use = -1 # 1:never had, 2:yes, 3:no
  birth_control = -1 # 1:never had, 2:none, 3:pill, 4:condom, 5:IUD, 6:shot, 7:withdrawal, 8:not sure
  sex_of_sexual_contacts = -1 # 1:none, 2:women only, 3:men only, 4:men and women
  sexuality = -1 # 1:straight, 2:gay, 3:bi, 4:not sure
  weight = -1 # 1:very under thru 5:very over
  weight_loss = -1 # 1:lose, 2:gain, 3:stay same, 4:nothing
  fruit_juice_drinking = -1 # 1:none thru 7:4+
  ate_fruit = -1 # 1:none thru 7:4+
  ate_salad = -1 # 1:none thru 7:4+
  ate_potatoes = -1 # 1:none thru 7:4+
  ate_carrots = -1 # 1:none thru 7:4+
  ate_other_vegetable = -1 # 1:none thru 7:4+
  soda_drinking = -1 # 1:none thru 7:4+
  milk_drinking = -1 # 1:none thru 7:4+
  ate_breakfast = -1 # 1:0 thru 8:7
  exercise_hour = -1 # 1:0 thru 8:7
  tv_per_day = -1 # 1:none thru 7:5+
  computer_use = -1 # 1:none thru 7:5+
  pe_attendance = -1 # 1:none thru 6:5
  plays_sports = -1 # 1:none thru 4:3+
  concussions_sports = -1 # 1:none thru 5:4+
  hiv_tested = -1 # 1:yes, 2:no, 3:not sure
  dentist_visit = -1 # 1:last 12, 2:12-14months, 3: more than 24, 4:never, 5:not sure
  asthma = -1 # 1:yes, 2:no, 3:not sure
  avg_sleep = -1 # 1:<4 thru 7:10+
  avg_grades = -1 # 1:A thru 5:F, 6:N/A, 7:not sure
  drive_marijuana = -1 # 1&2:0 thru 6:6+times
  hallucinogens_ever = -1 # 1:0 thru 6:40+
  sports_drink = -1 # 1:none thru 7:4+
  drink_water = -1 # 1:none thru 7:4+
  food_allergies = -1 # 1:yes, 2:no, 3:not sure
  muscle_exercise = -1 # 1:0 thru 8:7
  indoor_tanning = -1 # 1:0 thru 6:40+
  sunburns = -1 # 1:0 thru 8:7+
  difficulty_concentrating = -1  # 1:yes, 2:no
  english_ability = -1 # 1:very well thru 4:not at all

  # derived variables - CODED 1 FOR NO, 2 FOR YES
  ever_hard_drugs = 1
  sexual_assault = 1
  violence_perp = 1
  violence_victim = 1
  mental_illness_potential = 1
  promiscuous = 1
  parental_care = 1
  risk_score = 0
  opiate_risk_score = 0
  opiate_use = 1

  # used for ML algos. "actual" result to test for is first in array
  def get_risk_factors(self):
    return [
      self.opiate_use,
      self.opiate_risk_score,
      self.physical_fights,
      self.tried_cigs,
      self.smokes_cigs,
      self.cigs_per_day,
      self.days_vaping,
      self.cigar_use,
      self.quit_tobacco_attempt,
      self.days_drinking,
      self.current_drinking,
      self.binge_drinking,
      self.max_drinks,
      self.tried_marijuana,
      self.current_marijuana,
      self.sex_partners_total,
      self.sex_partners_recent,
      self.condom_use,
      self.drive_marijuana,
      self.hallucinogens_ever,
      self.ever_injected
    ]



  def get_core_no_opiates(self):
    return [self.opiate_use,
            self.opiate_risk_score,
            self.parental_care,
            self.mental_illness_potential,
            self.promiscuous, 
            self.sexual_assault,
            self.violence_perp, 
            self.violence_victim,
            self.age,
            self.sex, 
            self.grade, 
            self.tried_marijuana, 
            self.age_marijuana, 
            self.current_marijuana, 
            self.tried_cigs, 
            self.age_cigs, 
            self.smokes_cigs, 
            self.cigs_per_day, 
            self.had_sex, 
            self.age_of_sex, 
            self.sex_partners_total, 
            self.sex_partners_recent, 
            self.sex_intoxicated,
            self.sexuality, 
            self.weight, 
            self.weight_loss, 
            self.avg_grades]

  def get_data_no_opiates(self):
    return [self.parental_care,
            self.mental_illness_potential,
            self.promiscuous, 
            self.sexual_assault,
            self.violence_perp, 
            self.violence_victim,
            self.age,
            self.sex, 
            self.grade, 
            self.tried_marijuana, 
            self.age_marijuana, 
            self.current_marijuana, 
            self.tried_cigs, 
            self.age_cigs, 
            self.smokes_cigs, 
            self.cigs_per_day, 
            self.had_sex, 
            self.age_of_sex, 
            self.sex_partners_total, 
            self.sex_partners_recent, 
            self.sex_intoxicated,
            self.sexuality, 
            self.weight, 
            self.weight_loss, 
            self.hispanic, 
            self.seatbelt, 
            self.ride_with_drunk, 
            self.drive_drunk, 
            self.drive_text, 
            self.carry_weapon, 
            self.weapon_at_school, 
            self.carry_gun, 
            self.school_notsafe, 
            self.school_threats, 
            self.physical_fights, 
            self.fights_at_school, 
            self.been_raped, 
            self.been_forced_sexually, 
            self.date_rape_assault, 
            self.so_violence, 
            self.bullied_school, 
            self.bullied_cyber, 
            self.sad_hopeless, 
            self.consider_suicide, 
            self.plan_suicide, 
            self.attempt_suicide, 
            self.suicide_injury, 
            self.vaping, 
            self.days_vaping, 
            self.acquire_vape, 
            self.smokeless_tobacco, 
            self.cigar_use, 
            self.quit_tobacco_attempt, 
            self.days_drinking, 
            self.age_drinking, 
            self.current_drinking, 
            self.acquire_alcohol, 
            self.binge_drinking, 
            self.max_drinks, 
            self.ever_cocaine, 
            self.ever_inhalants,
            self.ever_meth, 
            self.ever_ecstasy, 
            self.ever_spice, 
            self.ever_steroids,
            self.ever_injected, 
            self.drugs_at_school,  
            self.condom_use, 
            self.birth_control, 
            self.sex_of_sexual_contacts, 
            self.fruit_juice_drinking, 
            self.ate_fruit, 
            self.ate_salad, 
            self.ate_potatoes, 
            self.ate_carrots, 
            self.ate_other_vegetable, 
            self.soda_drinking, 
            self.milk_drinking, 
            self.ate_breakfast, 
            self.exercise_hour, 
            self.tv_per_day, 
            self.computer_use, 
            self.pe_attendance, 
            self.plays_sports, 
            self.concussions_sports, 
            self.hiv_tested, 
            self.dentist_visit, 
            self.asthma, 
            self.avg_sleep, 
            self.avg_grades, 
            self.drive_marijuana, 
            self.hallucinogens_ever, 
            self.sports_drink, 
            self.drink_water, 
            self.food_allergies, 
            self.muscle_exercise, 
            self.indoor_tanning, 
            self.sunburns, 
            self.difficulty_concentrating, 
            self.english_ability
            ]

  # fills data set
  def __init__(self, csv_row):
    index = 0
    self.race = int(csv_row[index])
    index += 1
    self.age = int(csv_row[index])
    index += 1
    self.sex = int(csv_row[index])
    index += 1
    self.grade = int(csv_row[index])
    index += 1
    self.hispanic = int(csv_row[index])
    index += 1
    self.seatbelt = int(csv_row[index])
    index += 1
    self.ride_with_drunk = int(csv_row[index])
    index += 1
    self.drive_drunk = int(csv_row[index])
    index += 1
    self.drive_text = int(csv_row[index])
    index += 1
    self.carry_weapon = int(csv_row[index])
    index += 1
    self.weapon_at_school = int(csv_row[index])
    index += 1
    self.carry_gun = int(csv_row[index])
    index += 1
    self.school_notsafe = int(csv_row[index])
    index += 1
    self.school_threats = int(csv_row[index])
    index += 1
    self.physical_fights = int(csv_row[index])
    index += 1
    self.fights_at_school = int(csv_row[index])
    index += 1
    self.been_raped = int(csv_row[index])
    index += 1
    self.been_forced_sexually = int(csv_row[index])
    index += 1
    self.date_rape_assault = int(csv_row[index])
    index += 1
    self.so_violence = int(csv_row[index])
    index += 1
    self.bullied_school = int(csv_row[index])
    index += 1
    self.bullied_cyber = int(csv_row[index])
    index += 1
    self.sad_hopeless = int(csv_row[index])
    index += 1
    self.consider_suicide = int(csv_row[index])
    index += 1
    self.plan_suicide = int(csv_row[index])
    index += 1
    self.attempt_suicide = int(csv_row[index])
    index += 1
    self.suicide_injury = int(csv_row[index])
    index += 1
    self.tried_cigs = int(csv_row[index])
    index += 1
    self.age_cigs = int(csv_row[index])
    index += 1
    self.smokes_cigs = int(csv_row[index])
    index += 1
    self.cigs_per_day = int(csv_row[index])
    index += 1
    self.vaping = int(csv_row[index])
    index += 1
    self.days_vaping = int(csv_row[index])
    index += 1
    self.acquire_vape = int(csv_row[index])
    index += 1
    self.smokeless_tobacco = int(csv_row[index])
    index += 1
    self.cigar_use = int(csv_row[index])
    index += 1
    self.quit_tobacco_attempt = int(csv_row[index])
    index += 1
    self.days_drinking = int(csv_row[index])
    index += 1
    self.age_drinking = int(csv_row[index])
    index += 1
    self.current_drinking = int(csv_row[index])
    index += 1
    self.acquire_alcohol = int(csv_row[index])
    index += 1
    self.binge_drinking = int(csv_row[index])
    index += 1
    self.max_drinks = int(csv_row[index])
    index += 1
    self.tried_marijuana = int(csv_row[index])
    index += 1
    self.age_marijuana = int(csv_row[index])
    index += 1
    self.current_marijuana = int(csv_row[index])
    index += 1
    self.ever_cocaine = int(csv_row[index])
    index += 1
    self.ever_inhalants = int(csv_row[index])
    index += 1
    self.ever_heroin = int(csv_row[index])
    index += 1
    self.ever_meth = int(csv_row[index])
    index += 1
    self.ever_ecstasy = int(csv_row[index])
    index += 1
    self.ever_spice = int(csv_row[index])
    index += 1
    self.ever_steroids = int(csv_row[index])
    index += 1
    self.ever_opioids = int(csv_row[index])
    index += 1
    self.ever_injected = int(csv_row[index])
    index += 1
    self.drugs_at_school = int(csv_row[index])
    index += 1
    self.had_sex = int(csv_row[index])
    index += 1
    self.age_of_sex = int(csv_row[index])
    index += 1
    self.sex_partners_total = int(csv_row[index])
    index += 1
    self.sex_partners_recent = int(csv_row[index])
    index += 1
    self.sex_intoxicated = int(csv_row[index])
    index += 1
    self.condom_use = int(csv_row[index])
    index += 1
    self.birth_control = int(csv_row[index])
    index += 1
    self.sex_of_sexual_contacts = int(csv_row[index])
    index += 1
    self.sexuality = int(csv_row[index])
    index += 1
    self.weight = int(csv_row[index])
    index += 1
    self.weight_loss = int(csv_row[index])
    index += 1
    self.fruit_juice_drinking = int(csv_row[index])
    index += 1
    self.ate_fruit = int(csv_row[index])
    index += 1
    self.ate_salad = int(csv_row[index])
    index += 1
    self.ate_potatoes = int(csv_row[index])
    index += 1
    self.ate_carrots = int(csv_row[index])
    index += 1
    self.ate_other_vegetable = int(csv_row[index])
    index += 1
    self.soda_drinking = int(csv_row[index])
    index += 1
    self.milk_drinking = int(csv_row[index])
    index += 1
    self.ate_breakfast = int(csv_row[index])
    index += 1
    self.exercise_hour = int(csv_row[index])
    index += 1
    self.tv_per_day = int(csv_row[index])
    index += 1
    self.computer_use = int(csv_row[index])
    index += 1
    self.pe_attendance = int(csv_row[index])
    index += 1
    self.plays_sports = int(csv_row[index])
    index += 1
    self.concussions_sports = int(csv_row[index])
    index += 1
    self.hiv_tested = int(csv_row[index])
    index += 1
    self.dentist_visit = int(csv_row[index])
    index += 1
    self.asthma = int(csv_row[index])
    index += 1
    self.avg_sleep = int(csv_row[index])
    index += 1
    self.avg_grades = int(csv_row[index])
    index += 1
    self.drive_marijuana = int(csv_row[index])
    index += 1
    self.hallucinogens_ever = int(csv_row[index])
    index += 1
    self.sports_drink = int(csv_row[index])
    index += 1
    self.drink_water = int(csv_row[index])
    index += 1
    self.food_allergies = int(csv_row[index])
    index += 1
    self.muscle_exercise = int(csv_row[index])
    index += 1
    self.indoor_tanning = int(csv_row[index])
    index += 1
    self.sunburns = int(csv_row[index])
    index += 1
    self.difficulty_concentrating = int(csv_row[index])
    index += 1
    self.english_ability = int(csv_row[index])

    self.raw_data = csv_row


    # derive new variables

    if self.ever_cocaine != 1 or self.ever_inhalants != 1 or self.ever_heroin != 1 or self.ever_meth != 1 or self.ever_ecstasy != 1 or self.ever_spice != 1 or self.ever_opioids != 1:
      self.ever_hard_drugs = 2
    
    if self.been_raped != 2 or self.been_forced_sexually != 1 or self.date_rape_assault != 1 or self.sex_intoxicated != 1:
      self.sexual_assault = 2
    
    if self.carry_weapon != 1 or self.weapon_at_school != 1 or self.physical_fights != 1 or self.fights_at_school != 1:
      self.violence_perp = 2
    
    if self.school_notsafe != 1 or self.school_threats != 1 or self.bullied_school != 2:
      self.violence_victim = 2
    
    if self.sad_hopeless != 2 or self.consider_suicide != 2 or (self.weight == 1 and self.weight_loss == 1) or self.difficulty_concentrating == 1:
      self.mental_illness_potential = 2
    
    if self.sex_partners_total >= 5 or self.sex_partners_recent >= 4 or self.sex_intoxicated == 2:
      self.promiscuous = 2
    
    if self.fruit_juice_drinking >= 3 and self.ate_other_vegetable >= 4 and self.dentist_visit <= 2:
      self.parental_care = 2
    
    if self.drive_marijuana > 2:
      self.risk_score += 1
    if self.condom_use  == 3:
      self.risk_score += 1
    if self.ever_injected or self.ever_hard_drugs > 2:
      self.risk_score += 1
    if self.binge_drinking >= 4:
      self.risk_score += 1
    if self.drive_drunk > 2:
      self.risk_score += 1

    """
    if self.current_marijuana >= 3:
      self.opiate_risk_score += 1
    if self.smokes_cigs >= 3:
      self.opiate_risk_score += 1
    if self.consider_suicide:
      self.opiate_risk_score += 1
    if self.avg_grades <= 3:
      self.opiate_risk_score += 1
    if self.ever_injected >= 2:
      self.opiate_risk_score += 1
    """

    # actual opiate use, for AI training
    if self.ever_heroin > 1 or self.ever_opioids > 2:
      self.opiate_use = 2

    # opiate risk score, by statistics
    self.opiate_risk_score = Scoring.get_opiate_risk_score(self)

    """
    for i in range (0, len(csv_row)):
      item = csv_row[i]
      if item != '' and item:
        item_as_int = int(item)
        
    """

    pass
