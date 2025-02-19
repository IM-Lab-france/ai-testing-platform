// frontend/tests/utils/test_dataUtils.js
import { validateEmail, transformData, isEmptyObject } from '../../src/utils/dataUtils';

test('validateEmail validates email correctly', () => {
    expect(validateEmail('test@example.com')).toBe(true);
    expect(validateEmail('invalid-email')).toBe(false);
});

test('transformData transforms data correctly', () => {
    const data = { name: 'John', age: 30, email: 'john@example.com' };
    const keys = ['name', 'email'];
    expect(transformData(data, keys)).toEqual(['John', 'john@example.com']);
});

test('isEmptyObject checks if object is empty', () => {
    expect(isEmptyObject({})).toBe(true);
    expect(isEmptyObject({ key: 'value' })).toBe(false);
});
