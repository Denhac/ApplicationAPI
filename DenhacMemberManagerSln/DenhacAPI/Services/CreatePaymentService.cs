using DenhacClientAPI.ResponseObjects;
using Newtonsoft.Json;

namespace DenhacClientAPI.Services
{
    public static partial class DenhacService
    {
        public static DenhacResponse CreatePaymentService(string member_id, double amount, string payment_type_id, string notes)
        {
            var resultStr = CallGet(hostName + "/createpayment?member_id=" + member_id + "&amount=" + amount + "&payment_type_id=" + payment_type_id + "&notes=" + notes);
            CreatePaymentResponse responseObj = JsonConvert.DeserializeObject<CreatePaymentResponse>(resultStr);

            if (responseObj.created != null && responseObj.created.Equals("True"))
                responseObj.transactionStatus = true;
            else
                responseObj.transactionStatus = false;

            return responseObj;
        }
    }
}