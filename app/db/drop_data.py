from app.db.database import db

tables = ['GameGoal', 'Athlete', 'Coach', 'Competition', 'Game', 'Season', 'Stadium', 'Team']

for table in tables:
    try:
        db.engine.execute('''DROP TABLE ''' + table)
    except Exception:
        print('Table ' + table + ' may have already been dropped, continuing to next drop')
