using DenhacAPI.ResponseObjects;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DenhacClientAPI.ResponseObjects
{
    public class GetMemberBalanceResponse : DenhacResponse
    {
        public float balance { get; set; }
        public List<DenhacAccountRow> rows { get; set; }
    }
}
