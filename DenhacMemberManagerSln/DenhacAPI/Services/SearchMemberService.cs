using DenhacClientAPI.ResponseObjects;
using Newtonsoft.Json;

namespace DenhacClientAPI.Services
{
    public static partial class DenhacService
    {
        public static DenhacResponse SearchMemberService(string search_str)
        {
            var resultStr = CallGet(hostName + "/searchmember?search_str=" + search_str);
            SearchMemberResponse responseObj = JsonConvert.DeserializeObject<SearchMemberResponse>(resultStr);

            if (responseObj.rows != null)
                responseObj.transactionStatus = true;
            else
                responseObj.transactionStatus = false;

            return responseObj;
        }
    }
}
