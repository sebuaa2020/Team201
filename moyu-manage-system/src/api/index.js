import request from '../utils/request';

export const fetchData = query => {
    return request({
        url: './table.json',
        method: 'get',
        params: query
    });
};

export const deliver = room_id => {
    return request({
        url: '/robot/deliver/',
        method: 'get',
        params: {'room_id': room_id}
    })
}

export const navigate = (source_x, source_y, target_x, target_y) => {
    return request({
        url: '/robot/navigate/',
        method: 'get',
        params: {'source_x': source_x, 'source_y': source_y, 'target_x':target_x, 'target_y': target_y}
    })
}