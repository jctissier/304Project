import app.db.drop_data as drop_data
import app.db.create_tables as create_tables
import app.db.generate_data as generate_data


def populate_db():
    print("Dropping Table")
    drop_data()

    print("\nCreating Empty Tables")
    create_tables()

    print("\nGenerate Data & Insert in DB")
    generate_data()
