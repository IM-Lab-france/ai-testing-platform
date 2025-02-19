// frontend/tests/utils/test_dateUtils.js
import { formatDate, isFutureDate, daysDifference } from '../../src/utils/dateUtils';

test('formatDate formats date correctly', () => {
    const date = new Date('2023-10-01T12:00:00');
    expect(formatDate(date)).toBe('01/10/2023');
});

test('isFutureDate checks if date is in the future', () => {
    const futureDate = new Date();
    futureDate.setDate(futureDate.getDate() + 1);
    expect(isFutureDate(futureDate)).toBe(true);

    const pastDate = new Date();
    pastDate.setDate(pastDate.getDate() - 1);
    expect(isFutureDate(pastDate)).toBe(false);
});

test('daysDifference calculates difference in days', () => {
    const date1 = new Date('2023-10-01');
    const date2 = new Date('2023-10-10');
    expect(daysDifference(date1, date2)).toBe(9);
});
