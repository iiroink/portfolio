#include "mainwindow.hh"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    ui->spinBoxN->setMinimum(0);
    ui->spinBoxN->setMaximum(MAX_N_POINTS);

    ui->spinBoxG->setMinimum(0);
    ui->spinBoxG->setMaximum(MAX_G_POINTS);

    ui->spinBoxP->setMinimum(0);
    ui->spinBoxP->setMaximum(MAX_P_POINTS);

    ui->spinBoxE->setMinimum(0);
    ui->spinBoxE->setMaximum(5);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_countPushButton_clicked()
{
    uint final_grade = count_final_grade(n_, g_, p_, e_);
    ui->textBrowser->setText("Total grade: " + QString::number(final_grade));
}


void MainWindow::on_spinBoxN_valueChanged(int n)
{
    n_ = n;
}


void MainWindow::on_spinBoxG_valueChanged(int g)
{
    g_ = g;
}


void MainWindow::on_spinBoxP_valueChanged(int p)
{
    p_ = p;
}


void MainWindow::on_spinBoxE_valueChanged(int e)
{
    e_ = e;
}

