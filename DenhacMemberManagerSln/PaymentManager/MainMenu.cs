using System;
using System.Windows.Forms;

using DenhacClientAPI.Services;

namespace PaymentManager
{
    public partial class MainMenu : Form
    {
        public MainMenu()
        {
            InitializeComponent();
        }

        private void btn_memberPayment_Click(object sender, EventArgs e)
        {
            new PaymentEntry().ShowDialog();
        }

        private void btn_multiPayment_Click(object sender, EventArgs e)
        {
            new OpenBalances().ShowDialog();
        }

        private void btn_importpaypal_Click(object sender, EventArgs e)
        {
            new ImportStatement().ShowDialog();
        }

        private void btn_newmember_Click(object sender, EventArgs e)
        {
            new MemberForm(MemberForm.MemberMode.Create, null).ShowDialog();
        }

        private void btn_testConnection_Click(object sender, EventArgs e)
        {
            DenhacService.hostName = txt_server.Text;
            DenhacService.userName = txt_username.Text;
            DenhacService.password = txt_password.Text;

            try {
                var service = DenhacService.LoginService();
                if (service.transactionStatus)
                {
                    MessageBox.Show("Login SUCCESS");
                    this.DisableLoginOptions();
                }
                else
                {
                    MessageBox.Show("Ruh-roh, you failed to login! Details:\n" + service.errorMsg);
                    this.EnableLoginOptions();
                }
            }
            catch (Exception exception)
            {
                MessageBox.Show(exception.ToString());
            }
        }

        private void btn_logout_Click(object sender, EventArgs e)
        {
            try
            {
                var service = DenhacService.LogoutService();
                if (service.transactionStatus)
                {
                    this.EnableLoginOptions();
                }
                else
                {
                    MessageBox.Show("Failed to log out for whatever weird reason. Details:\n" + service.errorMsg);
                }
            }
            catch (Exception exception)
            {
                MessageBox.Show(exception.ToString());
            }
        }

        private void EnableLoginOptions()
        {
            txt_server.Enabled = true;
            txt_username.Enabled = true;
            txt_password.Enabled = true;

            btn_testConnection.Enabled = true;
            btn_logout.Enabled = false;

            btn_newmember.Enabled = false;
            btn_memberPayment.Enabled = false;
            btn_multiPayment.Enabled = false;
            btn_importpaypal.Enabled = false;
        }

        private void DisableLoginOptions()
        {
            txt_server.Enabled = false;
            txt_username.Enabled = false;
            txt_password.Enabled = false;

            btn_testConnection.Enabled = false;
            btn_logout.Enabled = true;

            btn_newmember.Enabled = true;
            btn_memberPayment.Enabled = true;
            btn_multiPayment.Enabled = true;
            btn_importpaypal.Enabled = true;
        }
    }
}