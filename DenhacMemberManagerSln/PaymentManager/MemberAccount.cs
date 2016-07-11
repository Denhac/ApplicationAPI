using DenhacClientAPI.ResponseObjects;
using DenhacClientAPI.Services;

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace PaymentManager
{
    public partial class MemberAccount : Form
    {
        private Member member;

        public MemberAccount(Member i_member)
        {
            this.member = i_member;
            InitializeComponent();
        }

        private void MemberAccount_Load(object sender, EventArgs e)
        {
            // Populate form labels and call getmemberbalance to populate transaction grid
            lbl_id.Text = member.id.ToString();
            lbl_lastName.Text = member.lastName;
            lbl_firstName.Text = member.firstName;
            lbl_adusername.Text = member.ad_username;
            lbl_contactemail.Text = member.contact_email;
            lbl_paypalemail.Text = member.paypal_email;
            lbl_paymentamount.Text = member.paymentAmount.ToString();
            lbl_phone.Text = member.phoneNumber;
            lbl_phone2.Text = member.businessNumber;

            try
            {
                var service = (GetMemberBalanceResponse)DenhacService.GetMemberBalanceService(member.id);
                if (service.transactionStatus)
                {
                    lbl_balance.Text = service.balance.ToString();
                    bs_memberaccount.DataSource = service.rows;
                }
            }
            catch (Exception exception)
            {
                MessageBox.Show(exception.ToString());
            }



        }

        private void btn_back_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
