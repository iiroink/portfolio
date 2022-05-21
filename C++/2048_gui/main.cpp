/* COMP.CS.110 Project 4: NUMBERS_GUI
*
* GUI version of the game 2048.
*
* Detailed description in "instructions.txt".
*
* Code written by
* Name: Iiro Inkinen
* Student number: 50393673
* Username: vbiiin
* ( https://course-gitlab.tuni.fi/comp.cs.110-ohj-2_2022-KEVAT/vbiiin )
* E-Mail: iiro.inkinen@tuni.fi
*
* */

#include "mainwindow.hh"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    w.show();
    return a.exec();
}
