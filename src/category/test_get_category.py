import unittest
from unittest.mock import AsyncMock, MagicMock
from category.get_category import GetCategory

class TestGetCategory(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.mock_cluster = MagicMock()
        self.mock_cluster.test = MagicMock()

        self.mock_collection = AsyncMock()
        self.mock_collection.find.return_value.to_list = AsyncMock(return_value=[
            {'id': '123', 'name': 'category'}
        ])

        self.mock_cluster.test.__getitem__.return_value = self.mock_collection

        self.get_category = GetCategory(self.mock_cluster)

    async def test_get(self):
        result = await self.get_category.get('category')
        self.assertEqual(result, [{'id': '123', 'name': 'category'}])

