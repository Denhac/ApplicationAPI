using DenhacClientAPI.ResponseObjects;
using DenhacClientAPI.Services;

using System;
using System.Windows.Forms;

namespace PaymentManager
{
    public partial class PaymentEntry : Form
    {
        private string memberIdForPayment;

        public PaymentEntry()
        {
            InitializeComponent();
        }

        private void btn_back1_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void txt_search_TextChanged(object sender, EventArgs e)
        {
            if (txt_search.Text.Length >= 2)
            {
                try
                {
                    var service = (SearchMemberResponse)DenhacService.SearchMemberService(txt_search.Text);
                    if (service.transactionStatus)
                    {
                        bs_searchMemberResponse.DataSource = service.rows;
                        if(service.rows.Count == 0)
                        {
                            ClearSearchResults();
                        }
                    }
                }
                catch (Exception exception)
                {
                    MessageBox.Show(exception.ToString());
                    ClearSearchResults();
                }
            }
            else
            {
                ClearSearchResults();
            }
        }

        private void ClearSearchResults()
        {
            bs_searchMemberResponse.DataSource = null;
            txt_member.Text = "";
            memberIdForPayment = "";
        }

        private void dgv_searchResults_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            if (e.RowIndex >= 0)
            {
                DataGridViewRow row = dgv_searchResults.Rows[e.RowIndex];
                memberIdForPayment = Convert.ToString(row.Cells[0].Value);
                txt_member.Text = Convert.ToString(row.Cells[1].Value) + ", " + Convert.ToString(row.Cells[2].Value);
            }
        }

        private void PaymentEntry_Load(object sender, EventArgs e)
        {
            try
            {
                var service = (GetPaymentTypesResponse)DenhacService.GetPaymentTypesService();
                if (service.transactionStatus)
                {
                    bs_paymentTypesResponse.DataSource = service.rows;
                }
            }
            catch (Exception exception)
            {
                MessageBox.Show(exception.ToString());
            }
        }

        private void btn_submit_Click(object sender, EventArgs e)
        {
            if (ValidateForm())
            {
                try
                {
                    var paymentTypeId = ((PaymentType)cb_paymentType.SelectedItem).id;

                    var service = (CreatePaymentResponse)DenhacService.CreatePaymentService(memberIdForPayment, Convert.ToDouble(txt_amount.Text), paymentTypeId, txt_memoNotes.Text);
                    if (service.transactionStatus)
                    {
                        MessageBox.Show("Payment Created!");
                        ClearForm();
                    }
                }
                catch (Exception exception)
                {
                    MessageBox.Show(exception.ToString());
                }
            }
        }

        private bool ValidateForm()
        {
            if (String.IsNullOrEmpty(memberIdForPayment))
            {
                MessageBox.Show("Choose a Member from the list!");
                return false;
            }
            if (String.IsNullOrEmpty(txt_amount.Text))
            {
                MessageBox.Show("Please enter a valid amount!");
                return false;
            }
            try
            {
                Convert.ToDouble(txt_amount.Text);
            }
            catch (Exception e)
            {
                MessageBox.Show("Please enter a valid amount!");
                return false;
            }
            if (String.IsNullOrEmpty(txt_memoNotes.Text))
            {
                MessageBox.Show("Please enter Memo/Notes!");
                return false;
            }

            return true;
        }

        private void ClearForm()
        {
            memberIdForPayment = "";
            txt_amount.Text = "";
            txt_memoNotes.Text = "";
            txt_member.Text = "";
            txt_search.Text = "";
        }
    }
}
