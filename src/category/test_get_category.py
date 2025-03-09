import pytest
from unittest.mock import MagicMock, AsyncMock
from category.get_category import GetCategory

@pytest.mark.asyncio
async def test_get():
    mock_cluster = MagicMock()
    mock_collection = MagicMock()
    
    mock_cluster.test.__getitem__.return_value = mock_collection
    
    mock_cursor = AsyncMock()
    mock_cursor.to_list.return_value = [{'id': '123', 'name': 'category'}]
    mock_collection.find.return_value = mock_cursor  
    
    get_category = GetCategory(mock_cluster)
    
    # Запускаем тест
    result = await get_category.get('category')
    
    assert result == [{'id': '123', 'name': 'category'}]

