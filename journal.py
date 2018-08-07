import os


def load(name):
    """
    load method for journal

    :param name: loads journal from filename
        if no file is found, a new one is created with 'name' provided.
    :return: returns journal with populated data
    """
    data = []
    filename = get_full_path(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


def save(name, journal_data):
    """

    :param name: system use for where to save the journal file
    :param journal_data: the contents of the save file
    :return: nothing, is a with statement with a for loop for writing journal entries
    """
    filename = get_full_path(name)
    print("..... saving to: {}".format(filename))
    # fout = open(filename, 'w') <= when calling like this you must call fout = close()
    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def add_entry(text, journal_data):
    """

    :param text: what we're adding
    :param journal_data: what we're adding to
    :return: nothing
    """
    journal_data.append(text)


def get_full_path(name):
    """

    :param name: directory for this app
    :return: the full path filename
    """
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    return filename
