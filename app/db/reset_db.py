import app.db.drop_data as drop
import app.db.create_tables as create
import app.db.generate_data as generate


def run():
    print("Dropping Tables")
    drop.drop()

    print("Creating Tables")
    create.create()

    print("Inserting Data")
    generate.make()

    print("\n===> Everything is completed\n")

if __name__ == "__main__":
    run()
