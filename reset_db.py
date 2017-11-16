import app.db.drop_data as drop
import app.db.create_tables as create


def run():
    print("Dropping Tables")
    drop.drop()

    print("Creating Tables")
    create.create()


if __name__ == "__main__":
    run()