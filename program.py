import journal


def main():
    print_header()
    run_event_loop()


def print_header():
    print('-----------------------------')
    print('        Journal App          ')
    print('-----------------------------')


def run_event_loop():
    print('What do you want to do with your Journal?')
    print("")
    cmd = "EMPTY"
    journal_name = input('Your name?: ')
    journal_data = journal.load(journal_name)

    while cmd != 'x' and cmd != 'exit':
        print("")
        cmd = input('[L]ist entries, [A]dd entries, E[x]it:  ').lower().strip()

        if cmd == 'l' or cmd == 'list':
            list_entries(journal_data)
        elif cmd == 'a' or cmd == 'add':
            add_entry(journal_data)
        elif cmd != 'x' and cmd != 'exit':
            print("Sorry, we don't understand '{}'.".format(cmd))
    print('In a galaxy far far away...')

    journal.save(journal_name, journal_data)


def list_entries(data):
    print("")
    print("Your journal entries: ")
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('* [{}] {}'.format(idx + 1, entry))


def add_entry(data):
    print("")
    text = input('Type your entry, <enter> to exit: ')
    journal.add_entry(text, data)
    # data.append(text)


if __name__ == '__main__':
    main()