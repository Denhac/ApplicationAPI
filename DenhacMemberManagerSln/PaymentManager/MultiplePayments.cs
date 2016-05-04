using DenhacClientAPI.ResponseObjects;
using DenhacClientAPI.Services;

using System;
using System.Windows.Forms;

namespace PaymentManager
{
    public partial class MultiplePayments : Form
    {
        public MultiplePayments()
        {
            InitializeComponent();
        }

        private void btn_back_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void MultiplePayments_Load(object sender, EventArgs e)
        {
            try
            {
                var service = (OpenBalanceResponse)DenhacService.GetOpenBalanceService();
                if (service.transactionStatus)
                {
                    bs_openBalanceResponse.DataSource = service.rows;
                }
            }
            catch (Exception exception)
            {
                MessageBox.Show(exception.ToString());
            }
        }
    }
}
