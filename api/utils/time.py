from datetime import datetime

def get_split_and_week_and_time(weeks):
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    valid_weeks = weeks[weeks.From > now]
    return valid_weeks[valid_weeks.From == valid_weeks.From.min()].Split.values[0], valid_weeks[valid_weeks.From == valid_weeks.From.min()].Week.values[0], valid_weeks[valid_weeks.From == valid_weeks.From.min()].From.values[0]
