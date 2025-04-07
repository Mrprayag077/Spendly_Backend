# Spendly Backend API 🚀

**Live API URL:** [https://spendly-backend-oq2l.onrender.com/users/](https://spendly-backend-oq2l.onrender.com/users/)

Welcome to the backend of Spendly! This API is built using **Django** and is designed to handle user profiles, transactions, and more. Plug this into your frontend and get rolling 🧩

---

## 🛠️ API Dictionary (Endpoints)

| **Endpoint** | **Method** | **Description** |
| ------------ | --------- | --------------- |
| `/api/` | GET | Basic health check: "Hello from Django!" |
| `/api/test/` | GET | Test API response: `{ "message": "API is working 🚀" }` |
| `/api/firebase_endpoint/` | POST | Handle user profile and transaction actions |

### `/api/firebase_endpoint/` Actions

```json
Request structure:

{
  "userUUID": "user-id",
  "action": "get / update_profile / add_transaction / edit_transaction / delete_transaction",
  "profileData": { ... },          // required for update_profile
  "transactionId": "txn-id",       // required for transaction actions
  "transactionData": { ... }       // required for transaction actions
}
