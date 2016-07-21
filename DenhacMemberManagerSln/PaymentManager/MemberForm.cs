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
    public partial class MemberForm : Form
    {
        public enum MemberMode { Create, Update };
        private MemberMode mode;
        private Member member;

        public MemberForm(MemberMode i_mode, Member i_member)
        {
            InitializeComponent();
            mode = i_mode;
            member = i_member;
            this.loadForm();
        }

        private void btn_back_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void btn_save_Click(object sender, EventArgs e)
        {
            try
            {
                if (mode == MemberMode.Create)
                {
                    var service = (CreateMemberResponse)DenhacService.CreateMemberService(this.txt_lastname.Text,
                                                                                          this.txt_mi.Text,
                                                                                          this.txt_firstname.Text,
                                                                                          this.dt_birthdate.Value.Date,
                                                                                          this.txt_streetaddr.Text,
                                                                                          this.txt_city.Text,
                                                                                          this.txt_zipcode.Text,
                                                                                          this.txt_communicationemail.Text,
                                                                                          this.txt_paypalemail.Text,
                                                                                          this.txt_phone.Text,
                                                                                          this.txt_businessphone.Text,
                                                                                          this.txt_emercontact1.Text,
                                                                                          this.txt_emerphone1.Text,
                                                                                          this.txt_emeraddr1.Text,
                                                                                          this.txt_emerrelation1.Text,
                                                                                          this.txt_emercontact2.Text,
                                                                                          this.txt_emerphone2.Text,
                                                                                          this.txt_emeraddr2.Text,
                                                                                          this.txt_emerrelation2.Text,
                                                                                          this.txt_paymentamt.Text,
                                                                                          this.dt_joindate.Value.Date,
                                                                                          this.txt_proxcardid.Text,
                                                                                          this.txt_medicalproblems.Text,
                                                                                          this.txt_adusername.Text);
                    if (service.transactionStatus)
                    {
                        MessageBox.Show("New Member Created!");
                        this.Close();
                    }
                    else
                    {
                        MessageBox.Show(service.errorMsg);
                    }
                }
                else if (mode == MemberMode.Update)
                {
                    var service = (EditMemberResponse)DenhacService.EditMemberService(this.lbl_memberid.Text,
                                                                                        this.txt_lastname.Text,
                                                                                        this.txt_mi.Text,
                                                                                        this.txt_firstname.Text,
                                                                                        this.dt_birthdate.Value.Date,
                                                                                        this.txt_streetaddr.Text,
                                                                                        this.txt_city.Text,
                                                                                        this.txt_zipcode.Text,
                                                                                        this.txt_communicationemail.Text,
                                                                                        this.txt_paypalemail.Text,
                                                                                        this.txt_phone.Text,
                                                                                        this.txt_businessphone.Text,
                                                                                        this.txt_emercontact1.Text,
                                                                                        this.txt_emerphone1.Text,
                                                                                        this.txt_emeraddr1.Text,
                                                                                        this.txt_emerrelation1.Text,
                                                                                        this.txt_emercontact2.Text,
                                                                                        this.txt_emerphone2.Text,
                                                                                        this.txt_emeraddr2.Text,
                                                                                        this.txt_emerrelation2.Text,
                                                                                        this.txt_paymentamt.Text,
                                                                                        this.dt_joindate.Value.Date,
                                                                                        this.txt_proxcardid.Text,
                                                                                        this.txt_medicalproblems.Text,
                                                                                        this.txt_adusername.Text);
                    if (service.transactionStatus)
                    {
                        MessageBox.Show("Member Data Saved Successfully!");
                        this.Close();
                    }
                    else
                    {
                        MessageBox.Show(service.errorMsg);
                    }
                }
            }
            catch (Exception exception)
            {
                MessageBox.Show(exception.ToString());
            }
        }

        private void loadForm()
        {
            if (mode == MemberMode.Update && member != null)
            {
                lbl_memberid.Text = member.id.ToString();
                txt_lastname.Text = member.lastName;
                txt_mi.Text = member.middleInitial;
                txt_firstname.Text = member.firstName;
                if (member.birthdate != null)
                {
                    dt_birthdate.Value = (DateTime)member.birthdate;
                }                
                txt_streetaddr.Text = member.streetAddress1;
                txt_city.Text = member.city;
                txt_zipcode.Text = member.zipCode;
                txt_communicationemail.Text = member.contact_email;
                txt_paypalemail.Text = member.paypal_email;
                txt_phone.Text = member.phoneNumber;
                txt_businessphone.Text = member.businessNumber;
                txt_emercontact1.Text = member.emerContact1;
                txt_emerphone1.Text = member.emerPhone1;
                txt_emeraddr1.Text = member.emerAddress1;
                txt_emerrelation1.Text = member.emerRelation1;
                txt_emercontact2.Text = member.emerContact2;
                txt_emerphone2.Text = member.emerPhone2;
                txt_emeraddr2.Text = member.emerAddress2;
                txt_emerrelation2.Text = member.emerRelation2;
                txt_paymentamt.Text = member.paymentAmount.ToString();
                if (member.join_date != null)
                {
                    dt_joindate.Value = (DateTime)member.join_date;
                }                
                txt_proxcardid.Text = member.prox_card_id;
                txt_medicalproblems.Text = member.medicalConditionList;
                txt_adusername.Text = member.ad_username;
            }
        }
    }
}
