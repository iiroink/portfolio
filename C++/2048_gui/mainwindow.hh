/* COMP.CS.110 Project 4: NUMBERS_GUI
*  File: mainwindow.hh
*
* Code written by
* Name: Iiro Inkinen
* Student number: 50393673
* Username: vbiiin
* ( https://course-gitlab.tuni.fi/comp.cs.110-ohj-2_2022-KEVAT/vbiiin )
* E-Mail: iiro.inkinen@tuni.fi
*
* Description: Gui for the game. Handles everything visible for the player.
*
* */

#ifndef MAINWINDOW_HH
#define MAINWINDOW_HH

#include "gameboard.hh"

#include <QMainWindow>
#include <QGraphicsScene>
#include <QGraphicsRectItem>
#include <QInputDialog>
#include <QMessageBox>
#include <QLabel>
#include <QKeyEvent>
#include <QColor>
#include <math.h>
#include <vector>
#include <QTimer>

// UI widgets are positioned based on the margins of the gameboard.
const int SQUARE_SIZE = 80;
const int WIDTH_MARGIN = 50;
const int TOP_MARGIN = 250;
const int BOTTOM_MARGIN = 50;
const int BOARD_MARGIN = 20;

const Coords LEFT = {-1, 0};
const Coords UP = {0, -1};
const Coords RIGHT = {1, 0};
const Coords DOWN = {0, 1};

struct Color {
    int number;
    QColor color;
};

const std::vector< Color > COLORS = { // Colors up to 2048
    { 0, QColor(255, 255, 255) },   // White
    { 2, QColor(223, 225, 255) },   //   |
    { 4, QColor(191, 223, 255) },   //   |
    { 8, QColor(159, 191, 255) },   //   |
    { 16, QColor(128, 159, 255) },  //   |
    { 32, QColor(96, 128, 255) },   //   |
    { 64, QColor(64, 96, 255) },    //   |
    { 128, QColor(32, 64, 255) },   //   V
    { 256, QColor(0, 32, 255) },    // Blue
    { 512, QColor(255, 255, 170) }, //   |
    { 1024, QColor(255, 255, 85) }, //   V
    { 2048, QColor(255, 255, 0) },  // Yellow
};

const QColor BIG_NUMBER_COLOR = QColor(218, 165, 32); // Golden

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    // Adds a new number to the board. Also checks if the player lost due to
    // the board becoming full.
    void new_number();

    // Resets the game window.
    void on_resetButton_clicked();

    // Clock visible for the player.
    void clock();

    // Pauses the game: stops the clock and disables keyboard inputs.
    void on_pauseButton_toggled(bool checked);

private:
    Ui::MainWindow *ui;

    // The engines version of the gameboard. All the calulations are done to
    // this object.
    GameBoard* gameBoard_;
    // The physical board visible to the player. Displays "gameBoard_".
    QGraphicsScene* board_;
    // Matrix of pointers to every square (background) on the board. Indexing:
    // squares_.at(row-1).at(column-1)
    std::vector< std::vector < QGraphicsRectItem* > > squares_;
    // Matrix of pointers to every number on the board. Indexing:
    // numbers_.at(row-1).at(column-1)
    std::vector< std::vector < QLabel* > > numbers_;

    // Initializes the squares onto the gameboard.
    void init_gameboard();

    // Updates the numbers on the gameboard.
    void update_board();

    // Detects inputs from the user. Accepts arrow keys and wasd.
    void keyPressEvent(QKeyEvent* input);

    // Methods for setting the seed and goal. Empty or incorrect input results
    // in previous or default values being used. Goal is given as power of two.
    void set_seed();
    void set_goal();

    // Timer for delaying the displayal of new numbers. Method add_number starts
    // timer_, timeout calls slot new_number which stops timer_ and adds the
    // new number.
    QTimer* timer_;
    void add_number();

    // Visible clock
    QTimer* clock_;
    int minutes_ = 0;
    int seconds_ = 0;

    // Default value for seed is 0 and for goal 2048.
    int seed_ = 0;
    int goal_ = DEFAULT_GOAL;
    // Tells if the player has made a move after the last new number.
    bool hasMoved_ = false;
    // Tells if the game is over. Used to disable inputs.
    bool isGameOn_ = true;
    // Total score. Every merge yields points based on the newly merged number.
    int score_ = 0;
};
#endif // MAINWINDOW_HH
