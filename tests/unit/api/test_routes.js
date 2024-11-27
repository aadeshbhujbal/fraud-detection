const request = require('supertest');
const app = require('../../../src/api/server');
const { createSampleTransaction } = require('../../helpers/testData');

describe('Transaction API Routes', () => {
    describe('POST /api/transaction', () => {
        test('should accept valid transaction', async () => {
            const transaction = createSampleTransaction();
            
            const response = await request(app)
                .post('/api/transaction')
                .send(transaction);
            
            expect(response.status).toBe(200);
            expect(response.body.transactionId).toBe(transaction.id);
        });
        
        test('should reject transaction without required fields', async () => {
            const invalidTransaction = {
                userId: 'user123'
                // missing required fields
            };
            
            const response = await request(app)
                .post('/api/transaction')
                .send(invalidTransaction);
            
            expect(response.status).toBe(400);
            expect(response.body.error).toBeTruthy();
        });
    });
}); 