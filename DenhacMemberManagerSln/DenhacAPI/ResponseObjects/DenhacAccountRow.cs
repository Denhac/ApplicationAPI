using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DenhacAPI.ResponseObjects
{
    public class DenhacAccountRow
    {
        public DateTime transaction_date { get; set; }
        public float amount { get; set; }
        public string type { get; set; }
        public string notes { get; set; }
    }
}
