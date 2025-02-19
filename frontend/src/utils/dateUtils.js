// frontend/src/utils/dateUtils.js
export const formatDate = (date) => {
    if (!(date instanceof Date)) {
        throw new Error('Invalid date');
    }
    return date.toLocaleDateString('en-GB'); // Format DD/MM/YYYY
};

export const isFutureDate = (date) => {
    const now = new Date();
    return date > now;
};

export const daysDifference = (date1, date2) => {
    const oneDay = 24 * 60 * 60 * 1000; // hours*minutes*seconds*milliseconds
    const diffInTime = Math.abs(date2 - date1);
    return Math.round(diffInTime / oneDay);
};
