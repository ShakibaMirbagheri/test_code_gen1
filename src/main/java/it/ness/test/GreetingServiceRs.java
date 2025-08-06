package it.ness.test-code-gen1.service.rs;

import io.quarkus.hibernate.orm.panache.PanacheQuery;
import io.quarkus.panache.common.Parameters;
import io.quarkus.panache.common.Sort;
import it.ness.api.service.RsRepositoryServiceV3;
import it.ness.test-code-gen1.model.Greeting;

import jakarta.inject.Singleton;
import jakarta.ws.rs.Consumes;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.MediaType;

import static it.ness.test
import java.util.HashMap;
import java.util.Map;
import java.time.LocalDateTime;-code-gen1.management.AppConstants.GREETING_PATH;

@Path(GREETING_PATH)
@Produces(MediaType.APPLICATION_JSON)
@Consumes(MediaType.APPLICATION_JSON)
@Singleton
public class GreetingServiceRs extends RsRepositoryServiceV3<Greeting, String> {

	public GreetingServiceRs() {
		super(Greeting.class);
	}

	protected String getId(Greeting object) {
		// field with @id
		return object.uuid;
	}

	@Override
	protected String getDefaultOrderBy() {
		return "name asc";
	}

	@Override
	public PanacheQuery<Greeting> getSearch(String orderBy) throws Exception {
		String query = null;
		Map<String, Object> params = null;
		if (nn("like.tagses")) {
			String[] tagses = get("like.tagses").split(",");
			StringBuilder sb = new StringBuilder();
			if (null == params) {
				params = new HashMap<>();
			}
			for (int i = 0; i < tagses.length; i++) {
				final String paramName = String.format("tags%d", i);
				sb.append(String.format("tags LIKE :%s", paramName));
				params.put(paramName, "%" + tagses[i] + "%");
				if (i < tagses.length - 1) {
					sb.append(" OR ");
				}
			}
			if (null == query) {
				query = sb.toString();
			} else {
				query = query + " OR " + sb.toString();
			}
		}
		PanacheQuery<Greeting> search;
		Sort sort = sort(orderBy);
		if (sort != null) {
			search = Greeting.find(query, sort, params);
		} else {
			search = Greeting.find(query, params);
		}
		if (nn("obj.uuid")) {
			search.filter("Greeting.obj.uuid", Parameters.with("uuid", get("obj.uuid")));
		}
		if (nn("obj.uuids")) {
			search.filter("Greeting.obj.uuids", Parameters.with("uuids", asList("obj.uuids")));
		}
		if (nn("like.name")) {
			search.filter("Greeting.like.name", Parameters.with("name", likeParamToLowerCase("like.name")));
		}
		if (nn("from.date_time")) {
			LocalDateTime date = LocalDateTime.parse(get("from.date_time"));
			search.filter("Greeting.from.date_time", Parameters.with("date_time", date));
		}
		if (nn("to.date_time")) {
			LocalDateTime date = LocalDateTime.parse(get("to.date_time"));
			search.filter("Greeting.to.date_time", Parameters.with("date_time", date));
		}
		if (nn("obj.date_time")) {
			LocalDateTime date = LocalDateTime.parse(get("obj.date_time"));
			search.filter("Greeting.obj.date_time", Parameters.with("date_time", date));
		}
		if (nn("obj.greetingEnum")) {
			search.filter("Greeting.obj.greetingEnum", Parameters.with("greetingEnum", get("obj.greetingEnum")));
		}
		if (nn("obj.active")) {
			Boolean valueof = _boolean("obj.active");
			search.filter("Greeting.obj.active", Parameters.with("active", valueof));
		} else {
			search.filter("Greeting.obj.active", Parameters.with("active", true));
		}
		return search;
	}
}