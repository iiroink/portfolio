#ifndef MAINWINDOW_HH
#define MAINWINDOW_HH

#include <QMainWindow>

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
    void on_weightLineEdit_textChanged(const QString &arg1);

    void on_heightLineEdit_textEdited(const QString &arg1);

    void on_countButton_clicked();

private:
    Ui::MainWindow *ui;

    double weight_ = 0;
    double height_ = 0;
};
#endif // MAINWINDOW_HH
