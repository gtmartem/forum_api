from sanic.exceptions import NotFound

from forum_api import db_api
from forum_api.api.v1.helper import HTTPViewHelper
from forum_api.errors.exceptions import server_error_wrapper


class GetAllSectionsView(HTTPViewHelper):
    body_required = False
    json_required = False

    @server_error_wrapper
    async def get(self, request):
        section = await db_api.get_all_sections()
        if section:
            return section
        raise NotFound("no sections")


class GetSectionByIdView(HTTPViewHelper):
    body_required = False
    json_required = False

    @server_error_wrapper
    async def get(self, request, section_id):
        section = await db_api.get_section_by_id(section_id)
        if section:
            return section
        raise NotFound(f"no section with {section_id} id")


class PostSectionView(HTTPViewHelper):
    body_required = True
    json_required = ["title", "description"]
    type_check = {"title": str, "description": str}
    status = 201

    @server_error_wrapper
    async def post(self, request):
        section = await db_api.post_section(request.json)
        return section


class PutSectionView(HTTPViewHelper):
    body_required = True
    json_required = ["title", "description"]
    type_check = {"title": str, "description": str}

    @server_error_wrapper
    async def put(self, request, section_id):
        section = await db_api.put_section(request.json, section_id)
        if section:
            return section
        raise NotFound(f"no section with {section_id} id")


class DeleteSectionView(HTTPViewHelper):
    body_required = False
    json_required = False

    @server_error_wrapper
    async def delete(self, request, section_id):
        await db_api.delete_section(section_id)
        return {"id": section_id}

