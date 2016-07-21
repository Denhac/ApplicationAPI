using DenhacClientAPI.ResponseObjects;
using DenhacClientAPI.Services;

using System;
using System.Windows.Forms;

namespace PaymentManager
{
    public partial class OpenBalances : Form
    {
        private DenhacClientAPI.ResponseObjects.Member member;  // To store currently-selected row to pass to MemberAccount form

        public OpenBalances()
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

                    // Default to selecting the first row
                    if (service.rows.Count > 0)
                    {
                        member = (DenhacClientAPI.ResponseObjects.Member)dgv_openBalances.Rows[0].DataBoundItem;
                        btn_viewAccount.Enabled = true;
                    }
                    else
                    {
                        btn_viewAccount.Enabled = false;
                    }
                }
            }
            catch (Exception exception)
            {
                MessageBox.Show(exception.ToString());
            }
        }

        private void dgv_openBalances_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            if (e.RowIndex >= 0)
            {
                DataGridViewRow row = dgv_openBalances.Rows[e.RowIndex];
                member = (DenhacClientAPI.ResponseObjects.Member)dgv_openBalances.CurrentRow.DataBoundItem;
            }
        }

        private void btn_viewAccount_Click(object sender, EventArgs e)
        {
            new MemberAccount(member).ShowDialog();
        }

        private void dgv_openBalances_DoubleClick(object sender, EventArgs e)
        {
            btn_viewAccount_Click(sender, e);
        }

        private void btn_editmember_Click(object sender, EventArgs e)
        {
            new MemberForm(MemberForm.MemberMode.Update, member).ShowDialog();
        }
    }
}
