using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DenhacClientAPI.ResponseObjects
{
    public class OpenBalanceResponse : DenhacResponse
    {
        public List<MemberResponse> rows { get; set; }
    }
}
