# snote is a simple note taking application
# all of your notes will be saved in a snotes.txt file

def snote(main = None, search_type = 'block', args= 'None'):

    # required libraries
    import os
    from datetime import date
    today = date.today().strftime('%d-%m-%y')

    # requirement section:
    # create /snote directory in your home directory
    # create /snotes.txt and snote_temp.txt in /snote directory
    # change editory , user and path as you like
    editor = 'vim'
    user = os.getlogin() 
    path = '/home/'+user+'/snote/' # creat /snote directory in your home directory


    # generate a note serial
    with open(path +'snotes.txt', 'r') as file:
        text_lines = file.readlines()
        serial_list = ['serial: 0']
        for line in text_lines:
            if 'serial' in line:
                serial_list.append(line.split('    ')[0])
        new_serial = int(serial_list[-1].split(' ')[-1]) + 1
        note_serial = str(new_serial)

    # open vim for new note
    if main == 'n':
        with open(path +'snote_temp.txt', 'w') as file:
            file.write('serial: '+note_serial+'    ' + 'date: '+today +'\n\n')
        os.system(editor + ' '+path + 'snote_temp.txt')

    # saving the note in ssnotes.txt
        cont = input('\nHave you saved the note? y/n: ')
        if cont == 'y':
            with open(path + 'snotes.txt', 'a') as file:
                with open(path + 'snote_temp.txt', 'r') as temp:
                    text = temp.read()
                    file.write(text + '\n====\n')
        else:
            print('note not saved')

    # search for specific note

    elif main == 's':
        with open(path + 'snotes.txt', 'r') as file:
            text = file.read()
            blocks_list = text.split('\n====\n')
            if '' in blocks_list:
                blocks_list.remove('')
            if ' ' in blocks_list:
                blocks_list.remove(' ')
        search_blocks = []
        for block in blocks_list:
            myres = []
            for arg in args:
                if arg in block:
                    myres.append('true')
                else:
                    myres.append('false')
            if 'false' in myres:
                continue
            else:
                search_blocks.append(block)
        if search_type == 'block':
            for block in search_blocks:
                print(block)
        if search_type == 'line':
            d = 0
            for block in search_blocks:
                lines = block.split('\n')
                d = d + 1
                print('\n--------------\n'+ str(d))
                print('\n' + lines[0])
                for line in lines:
                    for arg in args:
                        if arg in line:
                            print(line)
                            break
    # edit notes:
    elif main == 'e':
        with open(path + 'snotes.txt', 'r') as file:
            text = file.read()
            blocks_list = text.split('\n====\n')
            if '' in blocks_list:
                blocks_list.remove('')
            if ' ' in blocks_list:
                blocks_list.remove(' ')
        search_blocks = []
        for block in blocks_list:
            myres = []
            for arg in args:
                if arg in block:
                    myres.append('true')
                else:
                    myres.append('false')
            if 'false' in myres:
                continue
            else:
                search_blocks.append(block)
        if len(search_blocks) == 1:
            index = blocks_list.index(search_blocks[0])
            with open(path +'snote_temp.txt', 'w') as file:
                file.write(search_blocks[0])
            os.system(editor + ' '+path + 'snote_temp.txt')
            cont = input('\nHave you saved the note? y/n: ')
            if cont == 'y':
                    with open(path + 'snote_temp.txt', 'r') as temp:
                        text = temp.read()
                        blocks_list[index] = text
                        with open(path +'snotes.txt', 'w') as file:
                            for block in blocks_list:
                                file.write(block+ '\n====\n')
        else:
            print('more than one search result')



    # remove notes
    elif main == 'rm':
        with open(path + 'snotes.txt', 'r') as file:
            text = file.read()
            blocks_list = text.split('\n====\n')
            if '' in blocks_list:
                blocks_list.remove('')
            if ' ' in blocks_list:
                blocks_list.remove(' ')
        search_blocks = []
        for block in blocks_list:
            myres = []
            for arg in args:
                if arg in block:
                    myres.append('true')
                else:
                    myres.append('false')
            if 'false' in myres:
                continue
            else:
                search_blocks.append(block)
        for block in search_blocks:
            print(block)
        cont = input('Are you sure you want to delete? ')
        if cont == 'y':
            for block in search_blocks:
                blocks_list.remove(block)
            with open(path + 'snotes.txt', 'w') as file:
                for block in blocks_list:
                    file.write(block + '\n====\n')


    # backup notes
    elif main == 'backup':
        with open(path + 'snotes.txt', 'r') as file:
            text = file.read()
            blocks_list = text.split('\n====\n')
            if '' in blocks_list:
                blocks_list.remove('')
            if ' ' in blocks_list:
                blocks_list.remove(' ')
        search_blocks = []
        for block in blocks_list:
            myres = []
            for arg in args:
                if arg in block:
                    myres.append('true')
                else:
                    myres.append('false')
            if 'false' in myres:
                continue
            else:
                search_blocks.append(block)
        name = input('Give the name for backing up: ')
        with open(path + 'snote_backup_'+name+'.txt', 'w') as file:
            for block in search_blocks:
                file.write(block + '\n====\n')
        print('ssnote_backup_'+name+'.txt is ready.')


    else:
        print('invalid argumnet')
