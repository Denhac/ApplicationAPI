using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DenhacClientAPI.ResponseObjects
{
    public class MemberResponse
    {
        public float balance { get; set; }
        public int id { get; set; }
        public string lastName { get; set; }
        public string firstName { get; set; }
        public string gnuCashId { get; set; }
        public string paymentAmount { get; set; }
        public bool active { get; set; }
        public bool onAutoPay { get; set; }
        public string contact_email { get; set; }
        public string paypal_email { get; set; }
    }
}
