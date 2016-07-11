using DenhacClientAPI.ResponseObjects;
using Newtonsoft.Json;

namespace DenhacClientAPI.Services
{
    public static partial class DenhacService
    {
        public static DenhacResponse GetMemberBalanceService(int i_member_id)
        {
            var resultStr = CallGet(hostName + "/getmemberbalance/" + i_member_id);
            GetMemberBalanceResponse responseObj = JsonConvert.DeserializeObject<GetMemberBalanceResponse>(resultStr);

            if (responseObj.rows != null)
                responseObj.transactionStatus = true;
            else
                responseObj.transactionStatus = false;

            return responseObj;
        }
    }
}
