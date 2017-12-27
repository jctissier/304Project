import app.db.script_drop_data as drop
import app.db.script_create_tables as create

def run():
    print("Dropping Tables")
    drop.drop()

    print("Creating Tables")
    create.create()

    print("\n===> Everything is completed\n")

if __name__ == "__main__":
    run()
