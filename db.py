from datetime import date
from datetime import datetime
from uuid import UUID, uuid4
from datetime import timedelta
from pony.orm import *

db = Database()

class Doctor(db.Entity):
    doctor_id = PrimaryKey(int, auto=True)
    first_name = Required(str)
    last_name = Required(str)
    national_code = Required(str, max_len=10, unique=True)
    medical_number = Required(str, unique=True)
    password = Required(str)
    conversations = Set('Conversation')
    patients = Set('Patient')

class Patient(db.Entity):
    patient_id = PrimaryKey(int, auto=True)
    first_name = Required(str)
    last_name = Required(str)
    center = Required(str)
    conversations = Set('Conversation')
    doctor = Required(Doctor)

class Chat_msg(db.Entity):
    msg_id = PrimaryKey(int, auto=True)
    message = Required(str)
    time_Sent = Required(datetime)
    type = Required(int)
    conversation = Required('Conversation')

class Conversation(db.Entity):
    conversation_id = PrimaryKey(UUID, auto=True)
    title = Required(str)
    patient = Required(Patient)
    doctor = Required(Doctor)
    chat_msgs = Set(Chat_msg)
    msg_history = Required('Msg_history')

class Msg_history(db.Entity):
    id = PrimaryKey(int, auto=True)
    date = Required(datetime)
    conversations = Set(Conversation)



class Constitution(db.Entity):
    id = PrimaryKey(int, auto=True)
    Activity_changes = Optional(bool, default=False)
    Appetite_change = Optional(bool, default=False)
    Chills = Optional(bool, default=False)
    Diaphoresis = Optional(bool, default='Fasle')
    Unexpected_weight_change = Optional(bool, default=False)
    Fatigue = Optional(bool, default=False)
    fever = Optional(bool, default=False)
    medical_form = Optional('Medical_form')


class Skin(db.Entity):
    id = PrimaryKey(int, auto=True)
    color_changes = Optional(bool, default=False)
    pallor = Optional(bool, default=False)
    rash = Optional(bool, default=False)
    wound = Optional(bool, default=False)
    medical_form = Optional('Medical_form')


class Head_Ear_Nose_Throat(db.Entity):
    id = PrimaryKey(int, auto=True)
    Congestion = Optional(bool, default=False)
    Dental_problem = Optional(bool, default=False)
    Drooling = Optional(bool, default=False)
    Ear_discharge = Optional(bool, default=False)
    Ear_pain = Optional(bool, default=False)
    Facial_swelling = Optional(bool, default=False)
    Hearing_loss = Optional(bool, default=False)
    Mouth_sores = Optional(bool, default=False)
    Nosebleeds = Optional(bool, default=False)
    Postnasal_drip = Optional(bool, default=False)
    Rhinorrhea = Optional(bool, default=False)
    Sinus_pressure = Optional(bool)
    Sneezing = Optional(bool, default=False)
    Sore_throat = Optional(bool, default=False)
    Tinnitus = Optional(bool, default=False)
    Trouble_swallowing = Optional(bool, default=False)
    Voice_change = Optional(bool, default=False)
    medical_form = Optional('Medical_form')


class Eye(db.Entity):
    id = PrimaryKey(int, auto=True)
    discharge = Optional(bool, default=False)
    itching = Optional(bool, default=False)
    pain = Optional(bool, default=False)
    redness = Optional(bool, default=False)
    Photophobia = Optional(bool, default=False)
    Visual_disturbance = Optional(bool, default=False)
    medical_form = Optional('Medical_form')


class Respiratory(db.Entity):
    id = PrimaryKey(int, auto=True)
    cough = Optional(bool, default=False)
    wheezing = Optional(bool, default=False)
    breath_shortness = Optional(bool, default=False)
    Activity_change = Optional(bool, default=False)
    Appetite_change = Optional(bool, default=False)
    Chills = Optional(bool, default=False)
    Diaphoresis = Optional(bool, default=False)
    Fatigue = Optional(bool, default=False)
    fever = Optional(bool, default=False)
    Apnea = Optional(bool, default=False)
    Chest_tightness = Optional(bool, default=False)
    Choking = Optional(bool, default=False)
    Stridor = Optional(bool, default=False)
    medical_form = Optional('Medical_form')


class Gastrointestinal(db.Entity):
    id = PrimaryKey(int, auto=True)
    Arthralgias = Optional(bool, default=False)
    Back_pain = Optional(bool, default=False)
    nausea = Optional(bool, default=False)
    vomiting = Optional(bool, default=False)
    Gait_problems = Optional(bool, default=False)
    Joint_swelling = Optional(bool, default=False)
    Myalgias = Optional(bool, default=False)
    Neck_pain = Optional(bool, default=False)
    Neck_stiffness = Optional(bool, default=False)
    Abdominal_distention = Optional(bool, default=False)
    Abdominal_pain = Optional(bool, default=False)
    Anal_bleeding = Optional(bool, default=False)
    Blood_in_stool = Optional(bool, default=False)
    Constipation = Optional(bool, default=False)
    Diarrhea = Optional(bool, default=False)
    Rectal_pain = Optional(bool, default=False)
    medical_form = Optional('Medical_form')


class Genitourinary(db.Entity):
    id = PrimaryKey(int, auto=True)
    difficulty_urinating = Optional(bool, default=False)
    dysuria = Optional(bool, default=False)
    enuresis = Optional(bool, default=False)
    flank_pain = Optional(bool, default=False)
    frequency = Optional(int)
    genital_sore = Optional(bool, default=False)
    hematuria = Optional(bool, default=False)
    penile_discharge = Optional(bool, default=False)
    penile_pain = Optional(bool, default=False)
    penile_swelling = Optional(bool, default=False)
    scrotal_swelling = Optional(bool, default=False)
    testicular_pain = Optional(bool, default=False)
    urgency = Optional(bool, default=False)
    urine_decreased = Optional(bool, default=False)
    medical_form = Optional('Medical_form')


class Muscular(db.Entity):
    id = PrimaryKey(int, auto=True)
    gastrointestinal = Optional(bool, default=False)
    arthralgias = Optional(bool, default=False)
    back_pain = Required(bool, default=False)
    gait_problems = Optional(bool, default=False)
    joint_swelling = Optional(bool, default=False)
    myalgias = Optional(bool, default=False)
    neck_pain = Optional(bool, default=False)
    neck_stiffness = Optional(bool, default=False)
    medical_form = Optional('Medical_form')


class Endocrine(db.Entity):
    id = PrimaryKey(int, auto=True)
    cold_intolerance = Optional(bool, default=False)
    heat_intolerance = Optional(bool, default=False)
    polydipsia = Optional(bool, default=False)
    polyphagia = Optional(bool, default=False)
    polyuria = Optional(bool, default=False)
    medical_form = Optional('Medical_form')


class Neurological(db.Entity):
    id = PrimaryKey(int, auto=True)
    dizziness = Optional(bool, default=False)
    facial_asymmetry = Optional(bool, default=False)
    headaches = Optional(bool, default=False)
    light_headedness = Optional(bool, default=False)
    numbness = Optional(bool, default=False)
    seizures = Optional(bool, default=False)
    speech_difficulty = Optional(bool, default=False)
    syncope = Optional(bool, default=False)
    tremors = Optional(bool, default=False)
    weakness = Optional(bool, default=False)
    medical_form = Optional('Medical_form')


class Allergie(db.Entity):
    id = PrimaryKey(int, auto=True)
    allergy = Optional(str)
    medical_form = Optional('Medical_form')


class Medication(db.Entity):
    id = PrimaryKey(int, auto=True)
    dose = Optional(str)
    time_per_day = Optional(int, size=8, nullable=True, default=0)
    medical_form = Optional('Medical_form')


class Screening_test(db.Entity):
    id = PrimaryKey(int, auto=True)
    mammogram = Optional(str)
    pap_smear = Optional(str)
    bone_density = Optional(str)
    cholesterol = Optional(int, default=False)
    medical_form = Optional('Medical_form')
    result = Required('Result')


class Medical_form(db.Entity):
    id = PrimaryKey(int, auto=True)
    patient = Optional(Patient)
    allergie = Required(Allergie)
    medication = Required(Medication)
    screening_test = Required(Screening_test)
    Vaccination_historys = Required('Vaccination_history')
    personal__medical__history = Required('Personal_Medical_History')
    surgery = Required('Surgery')
    women_health_history = Required('Women_health_history')
    cardiovascular = Required('Cardiovascular')
    gastrointestinal = Required(Gastrointestinal)
    respiratory = Required(Respiratory)
    eye = Required(Eye)
    constitution = Required(Constitution)
    head__ear__nose__throat = Required(Head_Ear_Nose_Throat)
    genitourinary = Required(Genitourinary)
    endocrine = Required(Endocrine)
    muscular = Required(Muscular)
    hematologic = Required('Hematologic')
    allergy = Required('Allergy')
    neurological = Required(Neurological)
    skin = Required(Skin)
    psychiatric = Required('Psychiatric')
    social_history = Required('Social_history')
    other_issue = Required('Other_issue')
    additional__info = Required('Additional_Info')


class Result(db.Entity):
    id = PrimaryKey(int, auto=True)
    normal_unnormal = Optional(int)
    date = Optional(date)
    screening_test = Optional(Screening_test)


class Personal_Medical_History(db.Entity):
    id = PrimaryKey(int, auto=True)
    Alcoholism_DrugAbuse = Optional(bool, default=False)
    Asthma = Optional(bool, default=False)
    Cancer = Optional(bool, default=False)
    Depression_Anxiety_Bipolar_Suicidal = Optional(bool, default=False)
    Diabetes = Optional(bool, default=False)
    heart_disease = Optional(bool, default=False)
    Emphysema = Optional(bool, default=False)
    high_blood_pressure = Optional(bool, default=False)
    high_cholesterol = Optional(bool, default=False)
    hypothyroidism_thyroidDisease = Optional(bool, default=False)
    renal_disease = Optional(bool, default=False)
    migrain_headaches = Optional(bool, default=False)
    stroke = Optional(bool, default=False)
    medical_form = Optional(Medical_form)


class Vaccination_history(db.Entity):
    id = PrimaryKey(int, auto=True)
    Last_Tetanus_Booster = Optional(date)
    Last_Pnuemovax = Optional(date)
    Last_Flu = Optional(date)
    Last_Zoster = Optional(date)
    medical_form = Optional(Medical_form)


class Surgery(db.Entity):
    id = PrimaryKey(int, auto=True)
    type_surgery = Optional(str, nullable=True)
    date_surgery = Optional(date)
    medical_form = Optional(Medical_form)


class Women_health_history(db.Entity):
    id = PrimaryKey(int, auto=True)
    Date_Last_Menstrual = Optional(date)
    Age_Menopause = Optional(datetime, nullable=True)
    Age_First_Menstruation = Optional(datetime)
    Number_Pregnancies = Optional(int, size=8)
    Number_LiveBirths = Optional(int, size=8)
    Pregnancy_Complications = Optional(str, nullable=True)
    medical_form = Optional(Medical_form)


class Cardiovascular(db.Entity):
    id = PrimaryKey(int, auto=True)
    Chest_pain = Optional(bool, default=False)
    Leg_swelling = Optional(bool, default=False)
    Palpitations = Optional(bool, default=False)
    medical_form = Optional(Medical_form)


class Allergy(db.Entity):
    id = PrimaryKey(int, auto=True)
    food_allergies = Optional(str, default='Fasle')
    environmental_allergies = Optional(str)
    immunocompromised = Optional(str)
    medical_form = Optional(Medical_form)


class Hematologic(db.Entity):
    id = PrimaryKey(int, auto=True)
    adenopathy = Optional(bool, default=False)
    bruises_bleeds_easily = Optional(bool, default=False)
    medical_form = Optional(Medical_form)


class Psychiatric(db.Entity):
    id = PrimaryKey(int, auto=True)
    agitation = Optional(bool, default=False)
    behavior_problem = Optional(bool, default=False)
    confusion = Optional(bool, default=False)
    decreased_concentration = Optional(bool, default=False)
    dysphoric_mood = Optional(bool, default='Fasle')
    hallucinations = Optional(bool, default=False)
    hyperactive = Optional(bool, default=False)
    nervous_anxious = Optional(bool, default=False)
    self_injury = Optional(bool, default=False)
    sleep_disturbance = Optional(bool, default=False)
    suicidal_ideas = Optional(bool, default=False)
    medical_form = Optional(Medical_form)


class Plan(db.Entity):
    id = PrimaryKey(int, auto=True)
    credits = Required(int)
    expire_time = Required(timedelta)
    doctor = Optional(Doctor)


class Social_history(db.Entity):
    id = PrimaryKey(int, auto=True)
    occupation = Optional(str, nullable=True)
    education = Optional(str, nullable=True)
    marital_status = Optional(str, nullable=True)
    number_children = Optional(int)
    medical_form = Optional(Medical_form)


class Other_issue(db.Entity):
    id = PrimaryKey(int, auto=True)
    smoke_cigarettes = Optional(bool, default=False)
    current_packs_day = Optional(int)
    past_packs_day = Optional(int)
    other_tobacco = Optional(str, nullable=True)
    drink_alchohol = Optional(bool, default=False)
    type_alchohol = Optional(str, nullable=True)
    drinks_perweek = Optional(int)
    recreational_drugs = Optional(bool, default=False)
    needles_inject_drugs = Optional(bool, default=False)
    someone_else_drugs = Optional(bool, default=False)
    current_sexual_activities = Optional(bool, default=False)
    birth_control_method = Optional(str)
    current_exercise_regularly = Optional(bool, default=False)
    kind_exercise = Optional(str)
    howlong_exercise_min = Optional(int)
    howoften_exercise_perweek = Optional(int)
    hours_sleep_perday = Optional(int)
    diet_status = Optional(str)
    medical_form = Optional(Medical_form)


class Additional_Info(db.Entity):
    id = PrimaryKey(int, auto=True)
    travel_abroad_lastmonth = Optional(bool, default=False)
    where_travel = Optional(str)
    served_militry = Optional(bool)
    duration_militry_month = Optional(int)
    branch_militry = Optional(str)
    deployed_status = Optional(bool, default=False)
    where_deployed = Optional(str)
    medical_form = Optional(Medical_form)



db.generate_mapping(create_tables=True)
