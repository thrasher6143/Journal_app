import journal


def main():
    print_header()
    run_event_loop()


def print_header():

    """
    a command line header
    :return: uhhhh....

    """
    print('-----------------------------')
    print('        Journal App          ')
    print('-----------------------------')


def run_event_loop():
    """
    main event loop for journal, most of the other functions run through this,
    or are activated through another function call from this loop.
    Small greeting, asks your name then hits the while loop and
    prompts for option selection.
    :return:

    """
    journal_name = input('What is your name?: \n')
    print("""Hello {}, how are you today?
        You should write about it in your journal.""".format(journal_name))
    print('\nWhat do you want to do? ')
    # print("")
    cmd = "EMPTY"

    journal_data = journal.load(journal_name)

    while cmd != 'x' and cmd != 'exit':
        # print("")
        cmd = input('\n[L]ist entries, [A]dd entries, E[x]it:  \n').lower().strip()

        if cmd == 'l' or cmd == 'list':
            list_entries(journal_data)
        elif cmd == 'a' or cmd == 'add':
            add_entry(journal_data)
        elif cmd != 'x' and cmd != 'exit':
            print("Sorry, we don't understand '{}'.".format(cmd))
    print('In a galaxy far far away...\n')

    journal.save(journal_name, journal_data)


def list_entries(data):
    """

    :param data: calls out to the load function from journal_data
    when we get that back it gets listed
    :return: output to screen of entries

    """
    # print("")
    print("\nYour journal entries are: \n")
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('* [{}] {}'.format(idx + 1, entry))
    # print('\n')


def add_entry(data):
    """

    :param data: calls out to add_entry in journal and adds your text string
    :return: new entry to journal

    """
    # print("")
    text = input('\nType your entry, <enter> to exit: \n')
    journal.add_entry(text, data)
    # data.append(text)


if __name__ == '__main__':
    main()