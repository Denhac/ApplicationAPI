using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DenhacClientAPI.ResponseObjects
{
    public class PaymentType
    {
        public string id { get; set; }
        public string description { get; set; }
    }

    public class GetPaymentTypesResponse : DenhacResponse
    {
        public List<PaymentType> rows { get; set; }
    }
}
