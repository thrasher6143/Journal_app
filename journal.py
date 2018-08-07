import os


def load(name):
    """
    load method for journal

    :param name: loads journal from filename
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
    filename = get_full_path(name)
    print("..... saving to: {}".format(filename))
    # fout = open(filename, 'w') <= when calling like this you must call fout = close()
    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def add_entry(text, journal_data):
    journal_data.append(text)


def get_full_path(name):
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    return filename
