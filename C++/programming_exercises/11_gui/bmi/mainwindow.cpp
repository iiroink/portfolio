#include "mainwindow.hh"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_weightLineEdit_textChanged(const QString &arg1)
{
    weight_ = arg1.toFloat();
}


void MainWindow::on_heightLineEdit_textEdited(const QString &arg1)
{
    height_ = arg1.toFloat() / 100;
}


void MainWindow::on_countButton_clicked()
{
    if (height_ <= 0 or weight_ <= 0) {
        ui->resultLabel->setText("Cannot count");
        ui->infoTextBrowser->clear();
    } else {
        double bmi = weight_ / (height_ * height_);
        ui->resultLabel->setNum(bmi);
        if (bmi < 18.5) {
            ui->infoTextBrowser->setText("You are underweight.");
        } else if (bmi > 25) {
            ui->infoTextBrowser->setText("You are overweight.");
        } else {
            ui->infoTextBrowser->setText("Your weight is normal.");
        }
    }
}

