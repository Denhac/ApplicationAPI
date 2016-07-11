using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DenhacClientAPI.ResponseObjects
{
    public class SearchMemberResponse : DenhacResponse
    {
        public List<Member> rows { get; set; }
    }
}
