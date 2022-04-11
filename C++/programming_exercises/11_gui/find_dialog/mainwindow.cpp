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


void MainWindow::on_fileLineEdit_textChanged(const QString &arg1)
{
//    ui->textBrowser->setText(arg1);
    file_name_ = arg1.toStdString();
}


void MainWindow::on_keyLineEdit_textChanged(const QString &arg1)
{
    word_ = arg1.toStdString();
}


void MainWindow::on_findPushButton_clicked()
{
    std::ifstream file(file_name_);
    if (! file) {
        ui->textBrowser->setText("File not found");
    } else if (word_ == "") {
        ui->textBrowser->setText("File found");
    } else if (findWord(file)) {
        ui->textBrowser->setText("Word found");
    } else {
        ui->textBrowser->setText("Word not found");
    }
    file.close();
}

bool MainWindow::findWord(std::ifstream& file)
{
    std::string word = "";
    if (! ui->matchCheckBox->isChecked()) {
        for (auto& c : word_) {
            word.push_back(toupper(c));
        }
    } else {
        word = word_;
    }

    std::string line = "";
    while (getline(file, line)) {
        if (! ui->matchCheckBox->isChecked()) {
            std::string capital_line = "";
            for (auto& c : line) {
                capital_line.push_back(toupper(c));
            }
            line = capital_line;
        }
        if (line.find(word) != std::string::npos) {
            return true;
        }
    }
    return false;
}

