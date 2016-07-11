using DenhacAPI.ResponseObjects;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DenhacClientAPI.ResponseObjects
{
    public class Member
    {
        public float balance { get; set; }
        public int id { get; set; }
        public string lastName { get; set; }
        public string firstName { get; set; }
        public string middleInitial { get; set; }
        public DateTime? birthdate { get; set; }
        public string streetAddress1 { get; set; }
        public string streetAddress2 { get; set; }
        public string city { get; set; }
        public string zipCode { get; set; }
        public string phoneNumber { get; set; }
        public string businessNumber { get; set; }
        public string emerContact1 { get; set; }
        public string emerPhone1 { get; set; }
        public string emerAddress1 { get; set; }
        public string emerRelation1 { get; set; }
        public string emerContact2 { get; set; }
        public string emerPhone2 { get; set; }
        public string emerAddress2 { get; set; }
        public string emerRelation2 { get; set; }
        public string medicalConditionList { get; set; }
        public string gnuCashId { get; set; }
        public float paymentAmount { get; set; }
        public bool active { get; set; }
        public bool onAutoPay { get; set; }
        public bool isManager { get; set; }
        public bool isAdmin { get; set; }
        public string ad_username { get; set; }
        public string contact_email { get; set; }
        public string paypal_email { get; set; }
        public DateTime? join_date { get; set; }
        public string prox_card_id { get; set; }
        public string driver_license { get; set; }
    }
}
