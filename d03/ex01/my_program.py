from local_lib import path

def func():
    pass
    # create folder
    new_dir = path.Path("testfolder")
    new_dir.mkdir_p()   #test permissions?

    # create file in folder
    new_file = new_dir / 'test.txt'
    try:
        new_file.touch()
    except:
        print('Error creating new file')
        exit()

    # write in file
    try:
        new_file.write_text('hello world!')
    except:
        print('Error writing in file')
        exit()

    # read and print
    try:
        print(new_file.read_text())
    except:
        print('Error reading file')

if __name__ == '__main__':
    func()