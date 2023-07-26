import os
import tkinter as tk
from tkinter import messagebox as msgbox
import random as rnd
import time
def sysconfig():
    print("SYSTEM CONFIGURATION TOOL - (C) MICRO$OFT 1981-1983")
    print("[1] DISPLAY CURRENT CONFIGURATION")
    print("[2] CHANGE SYSTEM SETTINGS")
    print("[3] QUIT TO BOOT")
    sconfig = input("Please select the options marked in []. : ")
    config = "****CURRENT SYSTEM CONFIGURATION****\n[1]DATE/TIME = 03/27/84 18:35\n[2]FLOPPY A = TYPE 1 - 5.25/360K\nFLOPPY B = NONE - NONE\n[3]FIXED DISK 0 = NONE - NONE\n[4]CDROM = NONE - NONE\n[5]BOOT = A,C,B,CDROM"
    if sconfig == "1":
        print(config)
        input("Press ENTER |→ to continue.")
        sysconfig()
    elif sconfig == "2":
            print(config)
            cconfig = input("Please enter the setting number to change → ")
            if cconfig == "1":
                input("Enter new date : 00/11/2222 : ")
                input("Enter new time : 12:34 : ")
                sysconfig()
            elif cconfig == "2":
                print("TYPE 1 = 5.25/360K\nTYPE 2 = 5.25/1.2M\nTYPE 3 = 3.5/720K\nTYPE 4 = 3.5/1.44MHD")
                input("Enter type number : ")
                sysconfig()
            elif cconfig == "3":
                print("Refer to your documentation for hard disk types.Use type CS for a custom hard drive parameters.")
                hdconfig = input("Choose type : ")
                if hdconfig == "CS":
                    input("Hard disk size(Bytes) : ")
                    input("Head count : ")
                    input("Cylinders : ")
                    input("Sectors : ")
                    input("Driver File(A:\DRIVER\DRIVER.DRV) : ")
                    sysconfig()
            elif cconfig == "4":
                print("[1]SCSI CDROM\n[2]IDE CDROM\n[3]CUSTOM")
                dsconfig = input("Enter type : ")
                if dsconfig == "1":
                    print("SCSI CDROM DRIVER LOADED.")
                    sysconfig()
                elif dsconfig == "2":
                    print("IDE CDROM DRIVER LOADED.CDROM DRIVE ON SECONDARY MASTER.")
                    sysconfig()
                elif dsconfig == "3":
                        input("Driver files(A:\DRIVER\DRIVER.DRV) : ")
                        print("Driver failed to load.Possible reasons are bad/corrupt drivers or wrong drivers.Check your diskette and drive.")
                        sysconfig()
            elif cconfig == "5":
                input("Enter BOOT order - Possible values are A,B,C,CDROM : ")
                sysconfig()
    elif sconfig == "3":
        print("Rebooting NOW...")
        time.sleep(3)
        boot()
    else:
        sysconfig()
def boot():
    os.system("title DOS - Windows Virtual Machine")
    print("THE WINDOWS VIRTUAL BIOS VERSION 3.20")
    print("DRIVER WAS NOT INSTALLED.CD-ROM DRIVE NOT FOUND")
    print("No fixed disks detected.")
    print("327680B OK")
    print("Loading C...Not loaded.")
    print("No fixed disks detected.")
    print("ERROR\n0271 : Check date and time settings")
    dbios = input("Press ENTER |→ to enter SYSCONFIG")
    if dbios == "":
        sysconfig()
    time.sleep(10)
    error = [1,2,3,4,5,6,7,8,9]
    badfloppy = rnd.choice(error)
    if badfloppy == 1 or badfloppy == 2:
        print("Loading A:...Error!")
        print("Diskette drive error.Reinsert system diskette in A: and press a key to try again.")
        z = input("")
        boot()
    elif badfloppy == 3:
        print("Invalid system disk")
        print("Replace the disk and press any key...")
        z = input("")
        boot()
    elif badfloppy == 4:
        print("Reboot and Select proper Boot device")
        print("or Insert Boot media in selected boot device and press a key")
        z = input("")
        boot()
    elif badfloppy == 5:
        print("Loading A:...Success.")
        print("MS-DOS 3.30")
        print("Copyright (c) Microsoft / IBM 1981-1985")
        print("The following file is missing or corrupt : BOOT.MBR")
        print("The following file is missing or corrupt : BOOT.BSS")
        print("There is an error in your CONFIG.SYS on line 37.")
        print("While initializing device IOS:")
        print(" A subsystem driver failed to load. \n \n")
        print("Either a file in the .\iosubsys")
        print("subdirectory is corrupt, or the system is low on memory.")
        print("DOS Failed to load.Press any key to reboot the machine.")
        z = input("")
        boot()
    elif badfloppy == 6 or badfloppy == 7 or badfloppy == 8 or badfloppy == 9:
        print("Loading A:...Success.")
        print("MS-DOS 3.30")
        print("Copyright (c) Microsoft / IBM 1981-1985")
        print("Initializing sound device...")
        time.sleep(10)
        print("****CD-ROM DRIVER****\nThis driver is copyrighted (c) by International Business Machines International 1983-1991")
        time.sleep(3)
        print("Driver/drive NOT installed properly.CD-ROM Drive NOT found.")
        time.sleep(0.5)
        print("Device driver not found : TPCD001\nNo Valid CDROM device drivers selected\n")
        time.sleep(0.3)
        print("Bad command or file name")
        time.sleep(0.31)
        print("Invalid drive specification")
        time.sleep(0.11)
        print("Label not found.\nInvalid drive in search path")
        time.sleep(0.31)
        print("Bad command or file name")
        command()
def command():
        file = ''
        A = input('A>')
        if "  " in A:
            print("Bad character for specified value.")
            command()
        elif A == 'dir':
            print('Volume label is BOOTDISK')
            print('Directory of A:')
            print('FILENAME         SIZE  DATE  ')
            print('XCOPY.EXE        1328 3-27-84')
            print('COMMAND.COM      4213 3-27-84')
            print('EDIT.COM         7414 3-27-84')
            time.sleep(3)
            print('FORMAT.COM       5001 3-27-84')
            print('AUTOEXEC.BAT     2006 3-27-84')
            print('CONFIG.SYS       1064 3-27-84')
            print('EDIT.INI          440 3-27-84')
            print('BOOT.MBR          512 3-27-84')
            print('BOOT.BSS          745 3-27-84')
            print('FDISK.EXE        4660 3-27-84')
            print('SDSYS.EXE        3627 3-27-84')
            print('WINDIR.EXE       5000 7-25-23')
            print("273830 bytes ")
            print("113553 Bytes free")
            time.sleep(5)
            command()
        elif A == 'fdisk.exe':
            print('No fixed disks presents')
            command()
        elif A == 'format.com':
            print("WARNING : ALL DATA ON REMOVABLE DISK A: WILL BE LOST!")
            e = input("DO YOU WISH TO PROCEED?[Y/any invalid option to abort] : ")
            if e == "Y":
                for h in range(41):
                    print('Formatting track ' + str(h))
                    time.sleep(1)
                command()
            else:
                command()
        elif A == 'autoexec.bat':
            command()
        elif A == 'command.com':
            command()
        elif A == 'edit.com':
            print('EDIT VERSION 1.00')
            print('1 → Add value for  File')
            print('2 → Replace value for file')
            print('3 → Erase file')
            print('4 → List file')
            B = input('Choose an option(any invalid option to quit to DOS).')
            C = int(B)
            if C == 1:
                time.sleep(4)
                write = True
                while write == True:
                    d = input('Write anything you want.Type eX1t to quit to DOS')
                    file += d
                    if d == 'eX1t':
                        write = False
                        file += d
                        command()
                    elif d == 'c0Mn4mD':
                        write = False
                        command()
            if C == 2:
                time.sleep(1)
                write = True
                while write == True:
                    print('Please note that this option will wipe any existing file.')
                    d = input('Write anything you want.Type eX1t to quit to DOS.Type c0Mn4mD to exit without save')
                    file += d
                    if d == 'eX1t':
                        write = False
                        file += d
                        command()
                    elif d == 'c0Mn4mD':
                        write = False
                        command
            if C == 3:
                time.sleep(2)
                e = input('This option is IRREVERSIBLE.Type eR45€ to erase the file.')
                f = input('This option is IRREVERSIBLE.Type Er8s£ to erase the file.')
                if e == 'eR45€' and f == 'Er8s£':
                    file = ''
                    command()
            if C == 4:
                if file == '':
                    print('File empty.Quitting NOW...')
                else:
                    print(file)
                    command()
            command()
        elif A == 'xcopy.exe':
            print('Cannot copy ROOT : 381 Only drive A: present!')
            command()
        elif A == 'copy':
            print('Sorry,this disk is write-protected.')
            command()
        elif A == 'ver':
            print('MS-DOS 3.31')
            command()
        elif A == 'Okmeque1':
            print('Okmeque1 Python (FAKE) DOS version 1.18 running on whatever capacity A: drive.')
            command()
        elif A == 'specs':
            print('4.77/8 Mhz IBM AT.630K RAM.')
            command()
        elif A == 'help':
            print('FDISK.EXE : Fixed disk utility')
            print('EDIT.COM : Edits Text files')
            print('STOP : Stops the whole computer')
            print('VER : Shows the current version')
            print('FORMAT.COM : Formats A:')
            print('DIR : Lists directory of A:')
            print('SPECS : Shows the specifications of the computer')
            print('REBOOT_INTERNAL : Reboots the machine internally.')
            print('STOP_INTERNAL : Stops the machine internally')
            print('REBOOT : Reboots the host computer')
            print('STOP : Shuts down the host computer.')
            print('CONFIG /SYSTE : Show config.sys file')
            print('CONFIG /S : Show current configuration.')
            print('CONFIG : Enter Micro$oft system configuration')
            print('OKMEQUE1 : what this is actually')
            print('REN : Rename files')
            print('UPDATE : Lists the Update chart.')
            print('NOTE : This version of DOS is a bootdisk and only contains')
            print('minimal commands.To have more commands,eject this disk    ')
            print('and insert an installer disk.Then hold CTRL + ALT and then')
            print('press DEL.You need a Hard drive.Keep this disk as if the  ')
            print('installation fails,you may see what caused it.            ')
            print('Programs MUST have the extention on them unless it is an internal command')
            command()
        elif A == '':
            command()
        elif A == 'ren':
            input("Enter file to rename(A:\FILE.FILE) : ")
            tor = input("Enter new name : ")
            if len(tor) > 8:
                print("Too long!Returning to DOS...")
                command()
            else:
                print("An error occured while renaming file.Error 0x11.")
                command()
        elif A == 'update':
            print("****UPDATE CHART****")
            print("25/07/2023")
            print("ADDED CONFIG TOOL,CLS,CHECK A(yes I want you to have an A drive to run this because if you don't have an A drive you are not an authentic DOS user),REN and WINDIR")
            print("Repaired STOP_INTERNAL")
            print("Prompt now A> instead of A:> instead A:\> for authenticity")
            print("Help now shows easter eggs")
            print("Code now more compact")
            print("Update chart added")
            print("16/07/2023\nADDED BAD IBM CD-ROM DRIVER")
            input("Press enter to continue.")
            command()
        elif A == 'config':
            sysconfig()
        elif A == 'config /s':
            em = tk.Tk()
            em.withdraw()
            en = msgbox.showerror("DOS - Windows Virtual Machine","The following virtual machine has returned an unrecoverable error\n\nError details : \nSYSTEM_ACCESS_VIOLATION(0x0000005) has occured in WVM.EXE.Buffer of address 0F5A.\nThe virtual CPU has tried to access a part of memory that was not allocated.\nPossible reasons are bad drivers or the current machine is not capable of running this VM\n\nAny unsaved data was lost\nThe program will now exit.")
            os.system("@echo off")
            os.system("taskkill /f /im python.exe")
            os.system("taskkill /f /im py.exe")
            os.system("@echo on")

        elif A == 'config /syste':
            fg = True
            print("General permission protection error reading drive A:")
            while fg == True:
                dk = input("[A]bort,[R]etry,[I]gnore,[F]ail?")
                if dk == "A":
                    fg = False
                    command()
                elif dk == "R" or dk == "I":
                    print("General permission protection error reading drive A:")
                elif dk == "F":
                    print("Fail on INT 24")
                    fg = False
                    command()
            command()
        elif A == 'reboot_internal':
            boot()
        elif A == 'stop_internal':
            os.system("@echo off")
            os.system("taskkill /f /im python.exe")
            os.system("taskkill /f /im py.exe")
            os.system("@echo on")
        elif A == 'reboot':
            os.system('shutdown /r /t 0')
        elif A == 'stop':
            os.system('shutdown /s /t 0')
        elif A == 'sdsys.exe':
                print("Sound system now enabled.To test,please do SDSYS.EXE /TEST")
                command()
        elif A == 'sdsys.exe /test':
                print("Sound driver test.")
                print('\a')
                command()
        elif A == 'sdsys.exe /info':
            print("SDSYS Sound System Company")
            print("A compatible card is detected.")
            print("Driver version 2.174")
            print("This card supports EAX,MIDI and SynthWave formats")
            print("Card on slot 4")
            print("Driver enabled at location 00AAFF22CC")
            command()
        elif A == 'A:':
            command()
        elif A == 'cd' or A == 'chdir':
            print("No Subdirectories to change.")
            command()
        elif A == 'B:' or A == 'C:' or A == 'C:' or A == 'D:' or A == 'E:' or A == 'F:' or A == 'G:' or A == 'H:' or A == 'I:' or A == 'J:' or A == 'K:' or A == 'L:' or A == 'M:' or A == 'N:' or A == 'O:' or A == 'P:' or A == 'Q:' or A == 'R:' or A == 'S:' or A == 'T:' or A == 'U:' or A == 'V:' or A == 'W:' or A == 'X:' or A == 'Y:' or A == 'Z:':
            print('Invalid drive specification')
            command()
        elif A == 'windir.exe':
            print("****THE WINDOWS VIRTUAL MACHINE DIRECTORY****")
            print("Special driver has been loaded which allows full disk access for this session.")
            print("ATTENTION!THE DRIVER FILES ARE PROTECTED BY COPYRIGHT AND ANY COPYING WILL BE PUNISHED BY THE PROGRAM SELF DESTROYING AND PUNISHABLE BY LAW!")
            ld = input("DIR : ")
            dl = os.listdir(ld)
            print("Directory of " + ld)
            for x in range(len(dl)):
                if "." not in dl[x]:
                    print(dl[x] + "[DIR]")
                else:
                    print(dl[x])
            if ld == "A:" or ld == "a:":
                ld = "AB:"
            print("Driver now disabled." + ld + " no longer accessible from COMMAND.")
            command()
        else:
            print('Bad command or file name')
            command()
def bexec(b):
    if b == "Retry":
        chka()
    elif b == "Cancel":
        return '0x33'
def aexec(ins):
    if ins == "Retry":
        chka()
    elif ins == "Cancel":
        return '0x31'
def chka():
    a = os.path.exists('A:')
    if not os.listdir('A:'):
        dwin = tk.Tk()
        dwin.withdraw()
        a_notready = msgbox.askretrycancel("DOS - Windows Virtual Machine","A:\n\nThe device is not ready.",icon=msgbox.ERROR)
        if a_notready:
            bexec("Retry")
        else:
            bexec("Cancel")
    elif not a:
        rt = tk.Tk()
        rt.withdraw()
        err = msgbox.askretrycancel("DOS - Windows Virtual Machine","A:\n\nThe specified device does not exist.",icon=msgbox.ERROR)
        if err:
            aexec("Retry")
        else:
            aexec("Cancel")
    else:
        d1 = tk.Tk()
        d1.withdraw()
        d2 = msgbox.showwarning("Configuration Warning","The current configuration puts drive C: as the hard drive on this VM however DOS does not support hard disks over 327680KB so your hard disk might not be detected.")
        boot()
chka()
