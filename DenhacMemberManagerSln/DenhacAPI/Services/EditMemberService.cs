using System;

using DenhacClientAPI.ResponseObjects;
using Newtonsoft.Json;

using System.Collections.Generic;


namespace DenhacClientAPI.Services
{
    public static partial class DenhacService
    {
        public static DenhacResponse EditMemberService(
                                            string id,
                                            string lastName,
                                            string mi,
                                            string firstName,
                                            DateTime birthdate,
                                            string streetAddress,
                                            string city,
                                            string zipCode,
                                            string email,
                                            string paypal_email,
                                            string phone,
                                            string businessPhone,
                                            string emergencyContact1,
                                            string emergencyPhone1,
                                            string emergencyAddress1,
                                            string emergencyRelation1,
                                            string emergencyContact2,
                                            string emergencyPhone2,
                                            string emergencyAddress2,
                                            string emergencyRelation2,
                                            string paymentAmount,
                                            DateTime joinDate,
                                            string proxCardID,
                                            string medicalHealthProblems,
                                            string ad_username)
        {
            var postData = new List<KeyValuePair<string, string>>();
            postData.Add(new KeyValuePair<string, string>("lastName", lastName));
            postData.Add(new KeyValuePair<string, string>("middleInitial", mi));
            postData.Add(new KeyValuePair<string, string>("firstName", firstName));
            postData.Add(new KeyValuePair<string, string>("birthdate", birthdate.ToString("yyyy-MM-dd")));
            postData.Add(new KeyValuePair<string, string>("streetAddress1", streetAddress));
            postData.Add(new KeyValuePair<string, string>("city", city));
            postData.Add(new KeyValuePair<string, string>("zipCode", zipCode));
            postData.Add(new KeyValuePair<string, string>("contact_email", email));
            postData.Add(new KeyValuePair<string, string>("paypal_email", paypal_email));
            postData.Add(new KeyValuePair<string, string>("phoneNumber", phone));
            postData.Add(new KeyValuePair<string, string>("businessPhone", businessPhone));
            postData.Add(new KeyValuePair<string, string>("emerContact1", emergencyContact1));
            postData.Add(new KeyValuePair<string, string>("emerPhone1", emergencyPhone1));
            postData.Add(new KeyValuePair<string, string>("emerAddress1", emergencyAddress1));
            postData.Add(new KeyValuePair<string, string>("emerRelation1", emergencyRelation1));
            postData.Add(new KeyValuePair<string, string>("emerContact2", emergencyContact2));
            postData.Add(new KeyValuePair<string, string>("emerPhone2", emergencyPhone2));
            postData.Add(new KeyValuePair<string, string>("emerAddress2", emergencyAddress2));
            postData.Add(new KeyValuePair<string, string>("emerRelation2", emergencyRelation2));
            postData.Add(new KeyValuePair<string, string>("paymentAmount", paymentAmount));
            postData.Add(new KeyValuePair<string, string>("join_date", joinDate.ToString("yyyy-MM-dd")));
            postData.Add(new KeyValuePair<string, string>("prox_card_id", proxCardID));
            postData.Add(new KeyValuePair<string, string>("medicalHealthProblems", medicalHealthProblems));
            postData.Add(new KeyValuePair<string, string>("ad_username", ad_username));

            var resultStr = CallPost(hostName + "/editmember/" + id, postData);
            var responseObj = JsonConvert.DeserializeObject<EditMemberResponse>(resultStr);

            if (responseObj.success)
                responseObj.transactionStatus = true;
            else
                responseObj.transactionStatus = false;

            return responseObj;
        }
    }
}
