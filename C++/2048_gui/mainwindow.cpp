#include "mainwindow.hh"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    setWindowTitle("2048");

    // Size of the number grid a.k.a. gameboard.
    int boardSize = SIZE * SQUARE_SIZE;

    // Resize the main window to fit the board.
    setGeometry(500, 100, boardSize + WIDTH_MARGIN*2 + BOARD_MARGIN,
                boardSize + TOP_MARGIN + BOTTOM_MARGIN + BOARD_MARGIN);

    // Ask for seed and goal at the start.
    set_seed();
    set_goal();

    // SET UP THE MAIN WINDOW:
    board_ = new QGraphicsScene(this);                          // gameboard
    ui->graphicsView->setGeometry(WIDTH_MARGIN, TOP_MARGIN,
                                  boardSize + BOARD_MARGIN,
                                  boardSize + BOARD_MARGIN);
    ui->graphicsView->setScene(board_);
    board_->setSceneRect(0, 0, boardSize, boardSize);
    ui->resultLabel->setGeometry(WIDTH_MARGIN + BOARD_MARGIN / 2,// result text
                                 TOP_MARGIN - 50,
                                 boardSize,
                                 50);
    ui->resultLabel->setAlignment(Qt::AlignCenter);
    ui->scoreLabel->setGeometry(WIDTH_MARGIN + boardSize - 50,  // score number
                                 TOP_MARGIN - 80,
                                 70,
                                 50);
    ui->scoreLabel->setAlignment(Qt::AlignLeft);
    ui->scoreText->setGeometry(WIDTH_MARGIN + boardSize - 100,  // score text
                               TOP_MARGIN - 80,
                               50,
                               50);
    ui->scoreText->setAlignment(Qt::AlignLeft);
    ui->goalLabel->setGeometry(WIDTH_MARGIN, TOP_MARGIN - 170,  // goal text
                               boardSize, 50);
    ui->goalLabel->setAlignment(Qt::AlignCenter);
    ui->resetButton->setGeometry(WIDTH_MARGIN, TOP_MARGIN - 100,// reset button
                                 100, 30);
    ui->pauseButton->setGeometry(WIDTH_MARGIN, TOP_MARGIN - 65, // pause button
                                 100, 30);
    ui->pauseButton->setCheckable(true);
    ui->lcdNumberMin->setGeometry(WIDTH_MARGIN + boardSize - 60,// clock
                                  TOP_MARGIN - 40, 40, 30);
    ui->lcdNumberSec->setGeometry(WIDTH_MARGIN + boardSize - 20,
                                  TOP_MARGIN - 40, 40, 30);

    // Initialize the engine.
    gameBoard_ = new GameBoard;
    gameBoard_->init_empty();
    gameBoard_->fill(seed_);
    // Initialize the squares and number labels onto the gameboard.
    init_gameboard();
    update_board();

    // Set up the animation timer.
    timer_ = new QTimer(this);
    connect(timer_, SIGNAL(timeout()), this, SLOT(new_number()));
    // Set up the visible clock with 1000ms interval.
    clock_ = new QTimer(this);
    connect(clock_, SIGNAL(timeout()), this, SLOT(clock()));
    clock_->start(1000);

    // Set keyboard input focus to main window.
    setFocus();
}

MainWindow::~MainWindow()
{
    delete ui;
    delete board_;
    delete gameBoard_;
    delete timer_;
    delete clock_;
    // Delete numbers.
    for (int row = 1; row < SIZE; ++row) {
        for (int column = 1; column < SIZE; ++column) {
            delete numbers_.at(row).at(column);
            numbers_.at(row).at(column) = nullptr;
        }
    }
}

void MainWindow::new_number()
{
    // This method is called only once with the timer, so stop it.
    timer_->stop();
    // Add a new number on the board.
    gameBoard_->new_value();
    update_board();
    // Animation finished, allow new inputs.
    hasMoved_ = false;
    // A new square has been added. Check if the player lost.
    if (gameBoard_->is_full()) {                // If the player lost:
        isGameOn_ = false;                      // disable inputs
        clock_->stop();                         // stop the clock
        ui->pauseButton->setEnabled(false);     // disable pause button
        ui->resultLabel->setText("You lost");   // inform the player
        for (int row = 0; row < SIZE; ++row) {  // make the board red
            for (int column = 0; column < SIZE; ++column) {
                squares_.at(row).at(column)->setBrush(QColor(255, 159, 159));
                squares_.at(row).at(column)->update();
            }
        }
    }
}

void MainWindow::on_resetButton_clicked()
{
    // Pop up window asks for confirmation to reset.
    QMessageBox msgBox;
    msgBox.setWindowTitle("RESET");
    msgBox.setText("Do you want to reset?");
    msgBox.setGeometry(500 + WIDTH_MARGIN + BOARD_MARGIN,
                       100 + TOP_MARGIN, 200, 200);
    msgBox.setStandardButtons(QMessageBox::Yes | QMessageBox::No);

    // The reset is confirmed.
    if (msgBox.exec() == QMessageBox::Yes) {
        // The seed and goal can be reset too.
        QMessageBox msgBox;
        msgBox.setWindowTitle("RESET SUCCESSFULL");
        msgBox.setText("New seed and goal?");
        msgBox.setGeometry(500 + WIDTH_MARGIN + BOARD_MARGIN,
                           100 + TOP_MARGIN, 200, 200);
        msgBox.setStandardButtons(QMessageBox::Yes | QMessageBox::No);
        // Seed and goal reset is confirmed.
        if (msgBox.exec() == QMessageBox::Yes) {
            set_seed();
            set_goal();
        }
        // RESET:
        minutes_ = 0;                                           // clock
        seconds_ = 0;
        ui->lcdNumberMin->display(QString::number(minutes_));
        ui->lcdNumberSec->display(QString::number(seconds_));
        clock_->start();
        score_ = 0;                                             // score
        ui->resultLabel->setText("");                           // result text

        // Enable pause button and if it is checked, uncheck.
        ui->pauseButton->setEnabled(true);
        if (ui->pauseButton->isChecked()) {
            ui->pauseButton->toggle();
        }
        // Initialize a new board.
        gameBoard_->fill(seed_);
        update_board();

        // Allow inputs again.
        isGameOn_ = true;
    }
    // Set keyboard input focus to main window.
    setFocus();
}

void MainWindow::clock()
{
    if (seconds_ == 59) {
        ++minutes_;
        seconds_ = 0;
    } else {
        ++seconds_;
    }
    ui->lcdNumberMin->display(QString::number(minutes_));
    ui->lcdNumberSec->display(QString::number(seconds_));
}

void MainWindow::on_pauseButton_toggled(bool checked)
{
    // Pause button activated.
    if (checked) {
        clock_->stop();                         // stop the clock
        isGameOn_ = false;                      // disable keyboard inputs
        ui->resultLabel->setText("paused");     // inform the player
        for (int row = 0; row < SIZE; ++row) {  // make the board gray
            for (int column = 0; column < SIZE; ++column) {
                squares_.at(row).at(column)->setBrush(QColor(Qt::gray));
                squares_.at(row).at(column)->update();
            }
        }
    }
    // Pause button unactivated.
    else {
        clock_->start();                // start the clock
        isGameOn_ = true;               // enable keyboard inputs
        ui->resultLabel->setText("");   // empty the result text
        update_board();                 // bring back normal board colors
    }
    // Set keyboard input focus to main window.
    setFocus();
}

void MainWindow::init_gameboard()
{
    // Go through all squares that will be on the board.
    for (int row = 0; row < SIZE; ++row) {
        // Temporary vectors for one row of squares and numbers.
        std::vector < QGraphicsRectItem* > squareRow = {};
        std::vector < QLabel* > numberRow = {};
        for (int column = 0; column < SIZE; ++column) {
            // Add a square to the board.
            QGraphicsRectItem* newSquare = board_->addRect(row * SQUARE_SIZE,
                                                           column * SQUARE_SIZE,
                                                           SQUARE_SIZE,
                                                           SQUARE_SIZE);
            // Add a number to the board.
            QLabel* newNumber = new QLabel(this);
            newNumber->setGeometry(row*SQUARE_SIZE+WIDTH_MARGIN+BOARD_MARGIN/2,
                                   column*SQUARE_SIZE+TOP_MARGIN+BOARD_MARGIN/2,
                                   SQUARE_SIZE,
                                   SQUARE_SIZE);
            newNumber->setAlignment(Qt::AlignCenter);

            // Add the square and number to the row vector.
            squareRow.push_back(newSquare);
            numberRow.push_back(newNumber);
        }
        // Add the row vectors to the matrix.
        squares_.push_back(squareRow);
        numbers_.push_back(numberRow);
    }
}

void MainWindow::update_board()
{
    // Go through all squares on the board.
    for (int row = 0; row < SIZE; ++row) {
        for (int column = 0; column < SIZE; ++column) {
            // Get the number in the square from the engine.
            int number = gameBoard_->get_item({row, column})->get_value();
            // Zeros are not displayed.
            if (number == 0) {
                numbers_.at(row).at(column)->setText("");
            // Display the number in the square.
            } else {
                numbers_.at(row).at(column)->setNum(number);
            }
            // Variable to detect if the color is changed.
            bool colorChanged = false;
            // COLORS stores colors from 0 to 2048. Update numbers in that
            // range.
            for (auto i : COLORS) {
                if (i.number == number) {
                    squares_.at(row).at(column)->setBrush(i.color);
                    squares_.at(row).at(column)->update();
                    // The color has been changed.
                    colorChanged = true;
                }
            }
            // For numbers greater than 2048 use golden color.
            if (! colorChanged) {
                squares_.at(row).at(column)->setBrush(QColor(BIG_NUMBER_COLOR));
                squares_.at(row).at(column)->update();
            }
        }
    }
    // Update the score.
    ui->scoreLabel->setNum(score_);
}

void MainWindow::keyPressEvent(QKeyEvent *input)
{
    // The engine returns true if the goal number is reached, store it here.
    bool hasWon = false;
    // Player input.
    int key = input->key();
    // Can't move again until the board is updated or if game is not on.
    if ( (!hasMoved_) and isGameOn_ ) {
        if (key == Qt::Key_Up or key == Qt::Key_W) {            // Move up
            hasWon = gameBoard_->move(UP, goal_, score_);
            hasMoved_ = true;
        }
        if (key == Qt::Key_Left or key == Qt::Key_A) {          // Move left
            hasWon = gameBoard_->move(LEFT, goal_, score_);
            hasMoved_ = true;
        }
        if (key == Qt::Key_Down or key == Qt::Key_S) {          // Move down
            hasWon = gameBoard_->move(DOWN, goal_, score_);
            hasMoved_ = true;
        }
        if (key == Qt::Key_Right or key == Qt::Key_D) {         // Move right
            hasWon = gameBoard_->move(RIGHT, goal_, score_);
            hasMoved_ = true;
        }
        update_board();
        // The engine tells that the goal number has been reached.
        if (hasWon) {
            hasMoved_ = false;                      // no new number needed
            isGameOn_ = false;                      // disable keyboard input
            ui->resultLabel->setText("You won!");   // inform the player
            clock_->stop();                         // stop the clock
            ui->pauseButton->setEnabled(false);     // disable the pause button
            for (int row = 0; row < SIZE; ++row) {  // make the board golden
                for (int column = 0; column < SIZE; ++column) {
                    squares_.at(row).at(column)
                            ->setBrush(QColor(BIG_NUMBER_COLOR));
                    squares_.at(row).at(column)->update();
                }
            }
        }
        // If a move was made and the game is not over, add a new number.
        if (hasMoved_) {
            add_number();

        }
    }

}

void MainWindow::set_seed()
{
    QString input = "";
    // Open a pop window to ask the seed.
    input = QInputDialog::getText(this, tr("SEED"),
                                  tr("Enter seed value:"),
                                  QLineEdit::Normal);
    // Convert to string. If unsuccesfull, seed does not change.
    seed_ = input.toInt();
}

void MainWindow::set_goal()
{
    int goal = 0;
    QString input = "";
    // Open a pop window to ask the goal. Input is the power for two to get
    // the desired value.
    input = QInputDialog::getText(this, tr("GOAL"),
                                  tr("Enter goal (2^?):"),
                                  QLineEdit::Normal);
    goal = input.toInt();
    // Goal must be positive and achieveable with the grid size.
    if (goal > 0 && goal < pow(SIZE, 2)) {
        // Calculate the actual goal from the given power for two.
        goal_ = pow(2, goal);
        // Update goal text.
        ui->goalLabel->setText("GOAL NUMBER:    " + QString::number(goal_));
    }
}

void MainWindow::add_number()
{
    timer_->start(250);
}
