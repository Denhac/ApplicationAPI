using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DenhacClientAPI.ResponseObjects
{
    public class ImportPaypalDataResponse : DenhacResponse
    {
        public string response { get; set; }
        public int numPayments { get; set; }
        public int numUnapplied { get; set; }
        public float totalDues { get; set; }
        public float totalFees { get; set; }
    }
}
