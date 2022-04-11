#include "mainwindow.hh"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    ui->lcdNumberMin->setStyleSheet("background-color:green");
    ui->lcdNumberSec->setStyleSheet("background-color:magenta");

    timer = new QTimer(this);
    connect(timer, SIGNAL(timeout()), this, SLOT(updateTime()));
}

MainWindow::~MainWindow()
{
    delete ui;
    delete timer;
}

void MainWindow::updateTime()
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

void MainWindow::on_startButton_clicked()
{
    if (! is_timer_running_) {
        is_timer_running_ = true;
        timer->start(1000);
    }
}


void MainWindow::on_stopButton_clicked()
{
    if (is_timer_running_) {
        is_timer_running_ = false;
        timer->stop();
    }
}


void MainWindow::on_resetButton_clicked()
{
    minutes_ = 0;
    seconds_ = 0;
    ui->lcdNumberMin->display(QString::number(minutes_));
    ui->lcdNumberSec->display(QString::number(seconds_));
}

